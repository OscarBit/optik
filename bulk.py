# -*- coding: utf-8 -*-
import numpy as np
from utils import g_function, h_function, pqtu_function, rsvw_function


class Bulk:
    def __init__(self, *args, thickness_data=False):
        self.only_two = False
        self.n_layers = len(args) if len(args) >= 2 else "ERROR"
        if self.n_layers == "ERROR":
            raise "The cell must 2 layers or more"
        self.layers = []
        first = True
        for i in range(len(args)):
            layer = args[i]
            if not thickness_data:
                thickness = float(input("Thickness of {}:".format(layer.name)))
            else:
                if len(args) != len(thickness_data):
                    raise (
                        "Thickness_data list do not have the" + f" {len(args)} values."
                    )
                else:
                    thickness = thickness_data[i]
            if first:
                layer.use(thickness, first=first)
                first = False
            else:
                layer.use(thickness, bottom=layer == args[-1])
            self.layers.append(layer)
        self.p, self.q, self.t, self.u = False, False, False, False
        self.R, T = False, False

    def prepare_legos(self):
        for layer in self.layers:
            if layer.first:
                up = layer
                continue
            layer.g = g_function(layer.n, layer.k, n_back=up.n, k_back=up.k)
            if up.first:
                layer.h = (2 * (up.n ** (layer.k) - layer.n ** (up.k))) / (
                    ((up.n + layer.n) ** 2) + ((up.k + layer.k) ** 2)
                )
                layer.scnd = True
            else:
                layer.h = h_function(layer.n, layer.k, n_back=up.n, k_back=up.k)
            up = layer
        return False

    def calc_R(self):
        self.prepare_legos()
        for layer in self.layers:
            if layer.first:
                up = layer
                continue
            elif layer.scnd:
                p, q, t, u = pqtu_function(up, layer)
                p1n = p + (up.g * t) - up.h * u
                q1n = q + (up.h * t) + up.g * u
                t1n = t + (up.g * p) - up.h * q
                u1n = u + (up.h * p) + up.g * q
                top = up
                self.only_two = layer.scnd and layer.bottom
            elif up.scnd:
                # third matrix
                p1n_up, q1n_up, t1n_up, u1n_up = p1n, q1n, t1n, u1n
                p, q, t, u = pqtu_function(up, layer)
                r, s, v, w = rsvw_function(top, up)

                r_1up = r + top.g * v - top.h * w
                s_1up = s + top.h * v + top.g * w
                v_1up = v + top.g * r - top.h * s
                w_1up = w + top.h * r + top.g * s

                p1n = p1n_up * p - q1n_up * q + r_1up * t - s_1up * u
                q1n = q1n_up * p + p1n_up * q + s_1up * t + r_1up * u
                t1n = t1n_up * p - u1n_up * q + v_1up * t - w_1up * u
                u1n = u1n_up * p + t1n_up * q + w_1up * t + v_1up * u

                if not self.only_two:
                    self.p_T = p1n
                    self.q_T = q1n
                top = up
            else:
                # matrices in the middle
                p1n_top, q1n_top, t1n_top, u1n_top = p1n_up, q1n_up, t1n_up, u1n_up
                p1n_up, q1n_up, t1n_up, u1n_up = p1n, q1n, t1n, u1n
                r_1top, s_1top, v_1top, w_1top = r_1up, s_1up, v_1up, w_1up
                p, q, t, u = pqtu_function(up, layer)
                r, s, v, w = rsvw_function(top, up)

                r_1up = p1n_top * r - q1n_top * s + r_1top * v - s_1top * w
                s_1up = q1n_top * r + p1n_top * s + s_1top * v + r_1top * w
                v_1up = t1n_top * r - u1n_top * s + v_1top * v - w_1top * w
                w_1up = u1n_top * r + t1n_top * s + w_1top * v + v_1top * w

                p1n = p1n_up * p - q1n_up * q + r_1up * t - s_1up * u
                q1n = q1n_up * p + p1n_up * q + s_1up * t + r_1up * u
                t1n = t1n_up * p - u1n_up * q + v_1up * t - w_1up * u
                u1n = u1n_up * p + t1n_up * q + w_1up * t + v_1up * u
                top = up
            up = layer
        self.p, self.q, self.t, self.u = p1n, q1n, t1n, u1n
        R = ((self.t ** 2) + (self.u ** 2)) / ((self.p ** 2) + (self.q ** 2)) * 100
        return R

    def RT(self, new=True):
        no = 1
        if new:
            self.R = self.calc_R()
            if self.only_two:
                up, layer = self.layers[0:2]
                l = (
                    (1 + up.g) * (1 + layer.g)
                    - layer.h * (1 + up.g)
                    - up.h * (1 + layer.g)
                )
                m = up.h * (1 + layer.g) + layer.h * (1 + up.g) - up.h * layer.h
                self.T = (
                    (layer.n / no)
                    * ((l ** 2) + (m ** 2))
                    / ((self.p ** 2) + (self.q ** 2))
                    * 100
                )
                self.Abs = 100 - (self.R + self.T)
            else:
                top, up, layer = self.layers[0:3]
                l = (
                    (1 + top.g) * (1 + up.g) * (1 + layer.g)
                    - up.h * layer.h * (1 + top.g)
                    - layer.h * top.h * (1 + up.g)
                    - top.h * up.h * (1 + layer.g)
                )
                m = (
                    top.h * (1 + up.g) * (1 + layer.g)
                    + up.h * (1 + layer.g) * (1 + top.g)
                    + layer.h * (1 + top.g) * (1 + up.g)
                    - top.h * up.h * layer.h
                )
                self.T = (
                    (layer.n / no)
                    * ((l ** 2) + (m ** 2))
                    / ((self.p_T ** 2) + (self.q_T ** 2))
                    * 100
                )
                self.Abs = 100 - (self.R + self.T)
            return self.R, self.T
        else:
            self.Abs = 100 - (self.R + self.T)
            return self.R, self.T