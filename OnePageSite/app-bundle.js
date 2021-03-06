! function(t) {
    function e(r) {
        if (n[r]) return n[r].exports;
        var i = n[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        return t[r].call(i.exports, i, i.exports, e), i.l = !0, i.exports
    }
    var n = {};
    e.m = t, e.c = n, e.d = function(t, n, r) {
        e.o(t, n) || Object.defineProperty(t, n, {
            configurable: !1,
            enumerable: !0,
            get: r
        })
    }, e.n = function(t) {
        var n = t && t.__esModule ? function() {
            return t.default
        } : function() {
            return t
        };
        return e.d(n, "a", n), n
    }, e.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }, e.p = "", e(e.s = 3)
}([function(t, e, n) {
    "use strict";
    n.d(e, "b", function() {
        return r
    }), n.d(e, "a", function() {
        return i
    }), Math.lerp = function(t, e, n) {
        return t + (e - t) * n
    }, Math.TWO_PI = 2 * Math.PI;
    var r = function() {
            function t(t, e) {
                this.x = t, this.y = e
            }
            return t.lerp = function(e, n, r) {
                return new t(Math.lerp(e.x, n.x, r), Math.lerp(e.y, n.y, r))
            }, t.add = function(e, n) {
                return new t(e.x + n.x, e.y + n.y)
            }, t.multiply = function(e, n) {
                return new t(e.x * n.x, e.y * n.y)
            }, t.rotate = function(e, n) {
                var r = Math.sin(n),
                    i = Math.cos(n);
                return new t(e.x * i - e.y * r, e.x * r + e.y * i)
            }, t.transform = function(e, n, r, i) {
                return t.add(t.rotate(t.multiply(e, n), r), i)
            }, t.min = function(e, n) {
                return new t(Math.min(e.x, n.x), Math.min(e.y, n.y))
            }, t.max = function(e, n) {
                return new t(Math.max(e.x, n.x), Math.max(e.y, n.y))
            }, t.zero = new t(0, 0), t.one = new t(1, 1), t
        }(),
        i = {
            linear: function(t) {
                return t
            },
            easeInQuad: function(t) {
                return t * t
            },
            easeOutQuad: function(t) {
                return t * (2 - t)
            },
            easeInOutQuad: function(t) {
                return t < .5 ? 2 * t * t : (4 - 2 * t) * t - 1
            },
            easeInCubic: function(t) {
                return t * t * t
            },
            easeOutCubic: function(t) {
                return --t * t * t + 1
            },
            easeInOutCubic: function(t) {
                return t < .5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1
            },
            easeInQuart: function(t) {
                return t * t * t * t
            },
            easeOutQuart: function(t) {
                return 1 - --t * t * t * t
            },
            easeInOutQuart: function(t) {
                return t < .5 ? 8 * t * t * t * t : 1 - 8 * --t * t * t * t
            },
            easeInQuint: function(t) {
                return t * t * t * t * t
            },
            easeOutQuint: function(t) {
                return 1 + --t * t * t * t * t
            },
            easeInOutQuint: function(t) {
                return t < .5 ? 16 * t * t * t * t * t : 1 + 16 * --t * t * t * t * t
            }
        }
}, function(t, e, n) {
    "use strict";
    n.d(e, "a", function() {
        return o
    }), n.d(e, "b", function() {
        return s
    });
    var r, i = n(0);
    ! function(t) {
        t[t.pending = 0] = "pending", t[t.fulfilled = 1] = "fulfilled", t[t.rejected = 2] = "rejected"
    }(r || (r = {}));
    var o = function() {
            function t(t) {
                void 0 === t && (t = {});
                var e = this;
                this._children = [], this.elapsed = 0, this.status = r.pending, this.endless = !1, this.duration = 1e3, this.easingFn = i.a.linear, Object.keys(t).forEach(function(n) {
                    return e[n] = t[n]
                })
            }
            return Object.defineProperty(t.prototype, "progress", {
                get: function() {
                    return this.easingFn(Math.min(this.elapsed / this.duration, 1))
                },
                enumerable: !0,
                configurable: !0
            }), t.prototype.init = function() {}, t.prototype.push = function() {
                for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
                return (n = this._children).push.apply(n, t), this;
                var n
            }, t.prototype.resolve = function() {
                this.status = r.fulfilled
            }, t.prototype.reject = function() {
                this.status = r.rejected
            }, t.prototype.step = function(t) {
                this.elapsed += t, 1 === this.progress && this.resolve()
            }, t
        }(),
        s = function() {
            function t(t, e) {
                this.canvas = t, this.shapes = e, this.processes = [], this.timeScale = 1
            }
            return Object.defineProperty(t.prototype, "resolvableProcesses", {
                get: function() {
                    return this.processes.filter(function(t) {
                        return !t.endless
                    })
                },
                enumerable: !0,
                configurable: !0
            }), t.prototype.push = function() {
                for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
                for (var n = 0, r = t; n < r.length; n++) {
                    var i = r[n];
                    i.manager = this, i.init()
                }
                return (o = this.processes).push.apply(o, t), this;
                var o
            }, t.prototype.step = function(t) {
                for (var e = this.processes.length - 1; e >= 0; e--) {
                    var n = this.processes[e];
                    n.step(t * this.timeScale), n.status === r.fulfilled && (this.processes.splice(e, 1), this.push.apply(this, n._children))
                }
            }, t.prototype.resolveAll = function() {
                for (; this.resolvableProcesses.length > 0;) this.step(1e5)
            }, t
        }()
}, function(t, e, n) {
    "use strict";
    n.d(e, "b", function() {
        return r
    }), n.d(e, "a", function() {
        return o
    });
    var r, i = n(0);
    ! function(t) {
        t[t.pattern = 0] = "pattern", t[t.fill = 1] = "fill", t[t.stroke = 2] = "stroke", t[t.text = 3] = "text", t[t.none = 4] = "none"
    }(r || (r = {}));
    var o = function() {
        function t(t, e) {
            void 0 === e && (e = {});
            var n = this;
            this.points = t, this._worldPoints = [], this._children = [], this.pointsDirty = !0, this.boundingRectDirty = !0, this.type = r.stroke, this._translation = i.b.zero, this._rotation = 0, this._scale = i.b.one, Object.keys(e).forEach(function(t) {
                return n[t] = e[t]
            })
        }
        return Object.defineProperty(t.prototype, "rotation", {
            get: function() {
                return this._rotation
            },
            set: function(t) {
                this._rotation = t, this.setDirty()
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "absRotation", {
            get: function() {
                return this.absolute(function(t) {
                    return t.rotation
                }, function(t, e) {
                    return t + e
                })
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "scale", {
            get: function() {
                return this._scale
            },
            set: function(t) {
                this._scale = t, this.setDirty()
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "absScale", {
            get: function() {
                return this.absolute(function(t) {
                    return t.scale
                }, i.b.multiply)
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "translation", {
            get: function() {
                return this._translation
            },
            set: function(t) {
                this._translation = t, this.setDirty()
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "absTranslation", {
            get: function() {
                return this.absolute(function(t) {
                    return t.translation
                }, i.b.add)
            },
            enumerable: !0,
            configurable: !0
        }), Object.defineProperty(t.prototype, "worldPoints", {
            get: function() {
                if (this.pointsDirty) {
                    this._worldPoints.length = 0;
                    for (var t = 0, e = this.points; t < e.length; t++) {
                        var n = e[t],
                            r = i.b.transform(n, this.absScale, this.absRotation, this.absTranslation);
                        this._worldPoints.push(r)
                    }
                    this.pointsDirty = !1
                }
                return this._worldPoints
            },
            enumerable: !0,
            configurable: !0
        }), t.prototype.absolute = function(t, e) {
            var n = t(this);
            return this.parent ? e(n, this.parent.absolute(t, e)) : n
        }, Object.defineProperty(t.prototype, "worldBoundingRect", {
            get: function() {
                if (this.boundingRectDirty) {
                    for (var t = new i.b(Number.MAX_VALUE, Number.MAX_VALUE), e = new i.b(Number.MIN_VALUE, Number.MIN_VALUE), n = 0, r = this.worldPoints; n < r.length; n++) {
                        var o = r[n];
                        t = i.b.min(t, o), e = i.b.max(e, o)
                    }
                    this._worldBoundingRect = {
                        x: t.x,
                        y: t.y,
                        width: e.x - t.x,
                        height: e.y - t.y
                    }, this.boundingRectDirty = !1
                }
                return this._worldBoundingRect
            },
            enumerable: !0,
            configurable: !0
        }), t.prototype.worldContains = function(t, e) {
            for (var n = !1, r = this.worldPoints, i = 0, o = r.length - 1; i < r.length; o = i++) r[i].y > e != r[o].y > e && t < (r[o].x - r[i].x) * (e - r[i].y) / (r[o].y - r[i].y) + r[i].x && (n = !n);
            return n
        }, t.prototype.push = function() {
            for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
            for (var n = 0, r = t; n < r.length; n++) {
                r[n].parent = this
            }
            return (i = this._children).push.apply(i, t), this;
            var i
        }, t.prototype.setDirty = function() {
            this.pointsDirty = this.boundingRectDirty = !0;
            for (var t = 0, e = this._children; t < e.length; t++) {
                e[t].setDirty()
            }
        }, t.empty = function(e) {
            return new t([], e)
        }, t.hex = function(e, n, r, o) {
            var s = .25 * r,
                a = s * Math.sqrt(3);
            return new t([new i.b(e + 0, n - 2 * s), new i.b(e + a, n - s), new i.b(e + a, n + s), new i.b(e + 0, n + 2 * s), new i.b(e - a, n + s), new i.b(e - a, n - s)], o)
        }, t.rect = function(e, n, r, o, s) {
            return new t([new i.b(e, n), new i.b(e + r, n), new i.b(e + r, n + o), new i.b(e, n + o)], s)
        }, t
    }()
}, function(t, e, n) {
    "use strict";

    function r() {
        function t(t) {
            return void 0 === t && (t = {}), t.strokeStyle = g, s.a.hex(0, 0, m, t)
        }

        function e(t, e, n) {
            var r = s.a.rect(.5 * -m, .5 * -m, m, m, {
                type: s.b.fill,
                fillStyle: e
            });
            t.push(r);
            var i = s.a.rect(0, 0, n.width, n.height, {
                type: s.b.pattern,
                fillStyle: y.createPattern(n, "no-repeat"),
                scale: _,
                translation: new a.b(-n.width / 2, -n.height / 2)
            });
            t.push(i)
        }

        function n(t, e, n) {
            return s.a.rect(0, 0, O, P / 2, {
                type: s.b.text,
                font: D,
                text: t,
                fillStyle: g,
                translation: a.b.add(new a.b(0, 10), e),
                scale: n
            })
        }

        function r(t, e) {
            return new h.a({
                shape: t
            }).push(new h.c({
                shape: t,
                easingFn: w,
                duration: x,
                target: e
            }))
        }

        function c(t) {
            var e = t - Q;
            Q = t, b.step(e), v.step(e), window.requestAnimationFrame(c)
        }
        var f = document.getElementById("canvas") || function() {
                throw "Canvas not available."
            }(),
            y = f.getContext("2d") || function() {
                throw "2d context not available."
            }(),
            d = [],
            b = new o.b(f, d),
            v = new i.a(f, d, .36),
            g = "#fff",
            w = a.a.easeInOutCubic,
            m = 100,
            x = 300,
            _ = new a.b(-1, 1),
            O = 300,
            P = 50,
            D = "Montserrat";
        b.timeScale = .5, y.font = "2px " + D, y.fillText("x", 0, 0);
        var M = new a.b(m, 0),
            S = a.b.rotate(M, Math.PI / 3),
            j = a.b.rotate(M, Math.PI),
            k = a.b.rotate(M, 5 * Math.PI / 3),
            E = s.a.empty({
                strokeStyle: g
            }),
            A = t({
                url: l[1].url
            }),
            I = t({
                url: l[2].url
            }),
            C = t({
                url: l[3].url
            });
        d.push(E);
        var L = s.a.empty({
                type: s.b.none,
                scale: _
            }),
            R = t(),
            W = t({
                translation: S
            }),
            F = t({
                translation: j
            }),
            T = t({
                translation: k
            });
        L.push(R, W, F, T), e(R, l[0].color, l[0].img), e(W, l[1].color, l[1].img), e(F, l[2].color, l[2].img), e(T, l[3].color, l[3].img);
        var z = s.a.empty({
            type: s.b.none,
            translation: new a.b(60, .5 * -P)
        });
        d.push(z), z.push(n("JAANUS VARUS", a.b.zero, new a.b(1, 1))), z.push(n("Amsterdam, The Netherlands", new a.b(0, .5 * P), new a.b(1, .6))), b.push(new h.d({
            duration: 0
        }).push(new u.a({
            shape: E,
            easingFn: w,
            diameter: m,
            duration: 600
        }).push(new h.b({
            shape: E,
            easingFn: w,
            target: -Math.TWO_PI,
            duration: 300
        }).push(r(I, j), r(C, k), r(A, S))), (new h.e).push(new h.a({
            shape: L
        }).push(new u.c({
            shape: L,
            x: 1 * -m,
            y: 1.5 * -m,
            width: 2.5 * m,
            height: 3 * m,
            duration: 400
        })), new u.b({
            shape: z,
            width: O,
            height: P,
            duration: 400
        }), new p.a({
            shapes: [A, I, C]
        })))), b.push(new p.b);
        var Q = 0;
        window.requestAnimationFrame(c), b.push(), window.renderer = v, window.processManager = b
    }
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    for (var i = n(4), o = n(1), s = n(2), a = n(0), h = n(5), u = n(6), p = n(7), l = [{
            color: "#fff",
            imgPath: "me.jpg",
            img: new Image
        }, {
            color: "#1da1f2",
            imgPath: "./twitter.png",
            url: "https://google.com/",
            img: new Image
        }, {
            color: "#171516",
            imgPath: "./github.png",
            url: "https://github.com/JoshMooney",
            img: new Image
        }, {
            color: "#0274b3",
            imgPath: "./linkedin.png",
            url: "https://www.linkedin.com/in/josh-mooney-ire/",
            img: new Image
        }], c = 0, f = 0, y = l; f < y.length; f++) {
        var d = y[f];
        d.img.src = "./assets/" + d.imgPath, d.img.onload = function() {
            ++c >= l.length && r()
        }
    }
}, function(t, e, n) {
    "use strict";
    n.d(e, "a", function() {
        return i
    });
    var r = n(2),
        i = function() {
            function t(t, e, n, r) {
                void 0 === n && (n = .5), void 0 === r && (r = .5), this.canvas = t, this.shapes = e, this.translationFactorX = n, this.translationFactorY = r, this.ctx = t.getContext("2d")
            }
            return t.prototype.step = function(t) {
                var e = this,
                    n = e.canvas,
                    r = e.ctx;
                this.ensureCanvasValid(n, r), r.clearRect(-n.translationX, -n.translationY, n.width, n.height), this.renderShapes(r, this.shapes)
            }, t.prototype.renderShapes = function(t, e) {
                for (var n = 0, i = e; n < i.length; n++) {
                    var o = i[n],
                        s = o.worldPoints;
                    if (0 !== s.length) {
                        t.beginPath();
                        var a = s[s.length - 1];
                        t.moveTo(a.x, a.y);
                        for (var h = 0, u = s; h < u.length; h++) a = u[h], t.lineTo(a.x, a.y);
                        switch (o.type) {
                            case r.b.pattern:
                                t.fillStyle = this.styleOrDefault(o.fillStyle), t.save();
                                var p = o.worldBoundingRect;
                                t.translate(p.x, p.y), t.fill(), t.restore();
                                break;
                            case r.b.fill:
                                t.fillStyle = this.styleOrDefault(o.fillStyle), t.fill();
                                break;
                            case r.b.stroke:
                                t.strokeStyle = this.styleOrDefault(o.strokeStyle), t.lineWidth = this.lineWidthOrDefault(o), t.stroke();
                                break;
                            case r.b.text:
                                t.font = this.fontOrDefault(o), t.textAlign = this.textAlignOrDefault(o), t.fillStyle = this.styleOrDefault(o.fillStyle);
                                var l = o.absTranslation;
                                t.fillText(o.text, l.x, l.y + o.worldBoundingRect.height / 2)
                        }
                        o._children.length > 0 && (t.save(), t.clip(), this.renderShapes(t, o._children), t.restore())
                    }
                }
            }, t.prototype.styleOrDefault = function(t) {
                return t || "#EA2E49"
            }, t.prototype.fontOrDefault = function(t) {
                return t.worldBoundingRect.height + "px " + (t.font || "Arial")
            }, t.prototype.textAlignOrDefault = function(t) {
                return t.textAlign || "start"
            }, t.prototype.lineWidthOrDefault = function(t) {
                return t.lineWidth || 8
            }, t.prototype.ensureCanvasValid = function(t, e) {
                t.clientWidth === t.width && t.clientHeight === t.height || (t.width = t.clientWidth, t.height = t.clientHeight, t.translationX = t.width * this.translationFactorX, t.translationY = t.height * this.translationFactorY, e.translate(t.translationX, t.translationY), e.lineCap = "round", e.lineJoin = "round")
            }, t
        }()
}, function(t, e, n) {
    "use strict";
    n.d(e, "d", function() {
        return s
    }), n.d(e, "e", function() {
        return a
    }), n.d(e, "c", function() {
        return h
    }), n.d(e, "b", function() {
        return u
    }), n.d(e, "a", function() {
        return p
    });
    var r = n(0),
        i = n(1),
        o = this && this.__extends || function() {
            var t = Object.setPrototypeOf || {
                __proto__: []
            }
            instanceof Array && function(t, e) {
                t.__proto__ = e
            } || function(t, e) {
                for (var n in e) e.hasOwnProperty(n) && (t[n] = e[n])
            };
            return function(e, n) {
                function r() {
                    this.constructor = e
                }
                t(e, n), e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype, new r)
            }
        }(),
        s = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.step = function(e) {
                t.prototype.step.call(this, e)
            }, e
        }(i.a),
        a = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.step = function(t) {
                this.manager.resolvableProcesses.length <= 1 && this.resolve()
            }, e
        }(i.a),
        h = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.step = function(e) {
                t.prototype.step.call(this, e);
                var n = r.b.lerp(r.b.zero, this.target, this.progress);
                this.shape.translation = n
            }, e
        }(i.a),
        u = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.step = function(e) {
                t.prototype.step.call(this, e);
                var n = this.progress * this.target;
                this.shape.rotation = n
            }, e
        }(i.a),
        p = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.step = function(t) {
                this.manager.shapes.push(this.shape), this.resolve()
            }, e
        }(i.a)
}, function(t, e, n) {
    "use strict";

    function r(t, e, n, r) {
        void 0 === n && (n = 0), void 0 === r && (r = 0);
        var i = Array.apply(null, {
            length: e
        }).map(function(t) {
            return new a.b(n, r)
        });
        (o = t.points).push.apply(o, i), t.setDirty();
        var o
    }

    function i(t) {
        t.phase++, t.elapsed = 0
    }
    n.d(e, "b", function() {
        return u
    }), n.d(e, "c", function() {
        return p
    }), n.d(e, "a", function() {
        return l
    });
    var o = n(1),
        s = n(2),
        a = n(0),
        h = this && this.__extends || function() {
            var t = Object.setPrototypeOf || {
                __proto__: []
            }
            instanceof Array && function(t, e) {
                t.__proto__ = e
            } || function(t, e) {
                for (var n in e) e.hasOwnProperty(n) && (t[n] = e[n])
            };
            return function(e, n) {
                function r() {
                    this.constructor = e
                }
                t(e, n), e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype, new r)
            }
        }(),
        u = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return h(e, t), e.prototype.init = function() {
                this.x = this.x || 0, this.y = this.y || 0, this.target = s.a.rect(this.x, this.y, this.width, this.height), r(this.shape, 4, this.x, this.y), this.shape.points[2] = this.target.points[3], this.shape.points[3] = this.target.points[3]
            }, e.prototype.step = function(e) {
                t.prototype.step.call(this, e);
                var n = this.progress,
                    r = this.shape.points,
                    i = this.target.points;
                r[1] = a.b.lerp(i[0], i[1], n), r[2] = a.b.lerp(i[3], i[2], n), this.shape.setDirty()
            }, e
        }(o.a),
        p = function(t) {
            function e() {
                var e = null !== t && t.apply(this, arguments) || this;
                return e.phase = 0, e
            }
            return h(e, t), e.prototype.init = function() {
                this.x = this.x || 0, this.y = this.y || 0, this.target = s.a.rect(this.x, this.y, this.width, this.height), this.duration = this.duration / 2, r(this.shape, 5, this.x, this.y)
            }, e.prototype.step = function(t) {
                this.elapsed += t;
                var e = this.progress,
                    n = this.shape.points,
                    r = this.target.points;
                0 === this.phase ? (n[0] = a.b.lerp(r[0], r[1], e), n[1] = a.b.lerp(r[0], r[1], e), n[3] = a.b.lerp(r[0], r[3], e), n[4] = a.b.lerp(r[0], r[3], e), 1 === e && i(this)) : 1 === this.phase && (n[0] = a.b.lerp(r[1], r[2], e), n[4] = a.b.lerp(r[3], r[2], e), 1 === e && (n.length = 4, this.resolve())), this.shape.setDirty()
            }, e
        }(o.a),
        l = function(t) {
            function e() {
                var e = null !== t && t.apply(this, arguments) || this;
                return e.phase = 0, e
            }
            return h(e, t), e.prototype.init = function() {
                this.x = this.x || 0, this.y = this.y || 0, this.target = s.a.hex(this.x, this.y, this.diameter), this.duration = this.duration / 3, r(this.shape, 6, this.x, this.y)
            }, e.prototype.step = function(t) {
                this.elapsed += t;
                var e = this.progress,
                    n = this.shape.points,
                    r = this.target.points;
                0 === this.phase ? (n[0] = a.b.lerp(a.b.zero, r[2], e), n[1] = a.b.lerp(a.b.zero, r[2], e), n[2] = a.b.lerp(a.b.zero, r[2], e), n[3] = a.b.lerp(a.b.zero, r[5], e), n[4] = a.b.lerp(a.b.zero, r[5], e), n[5] = a.b.lerp(a.b.zero, r[5], e), 1 === e && i(this)) : 1 === this.phase ? (n[1] = a.b.lerp(r[2], r[3], e), n[2] = a.b.lerp(r[2], r[3], e), n[4] = a.b.lerp(r[5], r[0], e), n[5] = a.b.lerp(r[5], r[0], e), 1 === e && i(this)) : 2 === this.phase && (n[2] = a.b.lerp(r[3], r[4], e), n[5] = a.b.lerp(r[0], r[1], e), 1 === e && this.resolve()), this.shape.setDirty()
            }, e
        }(o.a)
}, function(t, e, n) {
    "use strict";
    n.d(e, "b", function() {
        return s
    }), n.d(e, "a", function() {
        return a
    });
    var r = n(1),
        i = n(8),
        o = this && this.__extends || function() {
            var t = Object.setPrototypeOf || {
                __proto__: []
            }
            instanceof Array && function(t, e) {
                t.__proto__ = e
            } || function(t, e) {
                for (var n in e) e.hasOwnProperty(n) && (t[n] = e[n])
            };
            return function(e, n) {
                function r() {
                    this.constructor = e
                }
                t(e, n), e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype, new r)
            }
        }(),
        s = function(t) {
            function e() {
                return null !== t && t.apply(this, arguments) || this
            }
            return o(e, t), e.prototype.init = function() {
                this.boundedOnKeyDown = this.onKeyDown.bind(this), window.addEventListener("keydown", this.boundedOnKeyDown), this.endless = !0
            }, e.prototype.step = function(t) {}, e.prototype.resolve = function() {
                t.prototype.resolve.call(this), window.removeEventListener("keydown", this.boundedOnKeyDown)
            }, e.prototype.onKeyDown = function(t) {
                27 === t.keyCode && this.manager.resolveAll()
            }, e
        }(r.a),
        a = function(t) {
            function e() {
                var e = null !== t && t.apply(this, arguments) || this;
                return e.hoverEffect = null, e
            }
            return o(e, t), e.prototype.init = function() {
                var t = this.manager.canvas;
                this.boundedOnMouseMove = this.onMouseMove.bind(this), this.boundedOnClick = this.onClick.bind(this), t.addEventListener("mousemove", this.boundedOnMouseMove), t.addEventListener("click", this.boundedOnClick), this.endless = !0
            }, e.prototype.step = function(t) {}, e.prototype.resolve = function() {
                t.prototype.resolve.call(this);
                var e = this.manager.canvas;
                e.removeEventListener("click", this.boundedOnClick), e.removeEventListener("mousemove", this.boundedOnMouseMove)
            }, e.prototype.onMouseMove = function(t) {
                for (var e = this.manager.canvas, n = t.pageX - e.offsetLeft - e.translationX, r = t.pageY - e.offsetTop - e.translationY, o = null, s = 0, a = this.shapes; s < a.length; s++) {
                    var h = a[s];
                    if (h.worldContains(n, r)) {
                        o = h;
                        break
                    }
                }
                null !== o ? (document.body.style.cursor = "pointer", null === this.hoverEffect && (this.hoverEffect = new i.a({
                    shape: o,
                    color: this.primaryColor,
                    maxLineWidth: 15,
                    minLineWidth: 6
                }), this.manager.push(this.hoverEffect))) : null !== this.hoverEffect && this.resolveHoverEffect()
            }, e.prototype.onClick = function(t) {
                null !== this.hoverEffect && (window.open(this.hoverEffect.shape.url), this.resolveHoverEffect())
            }, e.prototype.resolveHoverEffect = function() {
                document.body.style.cursor = "auto", this.hoverEffect.resolve(), this.hoverEffect = null
            }, e
        }(r.a)
}, function(t, e, n) {
    "use strict";

    function r(t, e) {
        t.phase = (t.phase + 1) % e, t.elapsed = 0
    }
    n.d(e, "a", function() {
        return h
    });
    var i = n(1),
        o = n(2),
        s = n(0),
        a = this && this.__extends || function() {
            var t = Object.setPrototypeOf || {
                __proto__: []
            }
            instanceof Array && function(t, e) {
                t.__proto__ = e
            } || function(t, e) {
                for (var n in e) e.hasOwnProperty(n) && (t[n] = e[n])
            };
            return function(e, n) {
                function r() {
                    this.constructor = e
                }
                t(e, n), e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype, new r)
            }
        }(),
        h = function(t) {
            function e() {
                var e = null !== t && t.apply(this, arguments) || this;
                return e.phase = 0, e.hoverShapes = [], e
            }
            return a(e, t), e.prototype.init = function() {
                for (var t = 0; t < 10; t++) this.hoverShapes.push(new o.a([this.shape.points[0]], {
                    translation: this.shape.translation,
                    strokeStyle: this.shape.strokeStyle,
                    lineWidth: this.minLineWidth + (this.maxLineWidth - this.minLineWidth) * t / 10
                }));
                (e = this.manager.shapes).push.apply(e, this.hoverShapes), this.duration = this.duration / this.shape.points.length, this.endless = !0;
                var e
            }, e.prototype.step = function(t) {
                this.elapsed += t;
                for (var e = this, n = e.hoverShapes, i = e.progress, o = this.shape.points, a = 0; a < n.length - 1; a++) n[a].points[0] = n[a + 1].points[0];
                n[n.length - 1].points[0] = s.b.lerp(o[this.phase], o[(this.phase + 1) % o.length], i), 1 === i && r(this, o.length);
                for (var h = 0, u = this.hoverShapes; h < u.length; h++) {
                    u[h].setDirty()
                }
            }, e.prototype.resolve = function() {
                t.prototype.resolve.call(this);
                for (var e = this.manager.shapes, n = 0, r = this.hoverShapes; n < r.length; n++) {
                    var i = r[n];
                    e.splice(e.indexOf(i), 1)
                }
            }, e
        }(i.a)
}]);