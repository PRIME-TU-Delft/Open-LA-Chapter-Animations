# MODULE
# name: colors

offblack = "#0C2340"
offwhite = "#E0E0E0"
blue = "#0076C2"
yellow = "#FFB81C"
purple = "#6F1D77"
green = "#308167"
pink = "#F87089"


def apply_to_texs(texs):
    # Create the correct variable colours for each equation
    for t in texs:
        t.set_color_by_tex(r" x ", blue)
        t.set_color_by_tex(r" \Delta x ", blue)
        t.set_color_by_tex(r" t ", yellow)
        t.set_color_by_tex(r" n ", purple)
        t.set_color_by_tex(r" E ", green)
        t.set_color_by_tex(r" u ", green)
        t.set_color_by_tex(r" \rho ", pink)



# tex_waveq_final.set_color_by_tex(r"E", "#308167")
# tex_waveq_final.set_color_by_tex(r" t ", "#FFCE2E")
# tex_waveq_final.set_color_by_tex(r"x", "#7AB1E8")
# tex_waveq_final.set_color_by_tex(r"\Delta x", "#7AB1E8")
# tex_waveq_final.set_color_by_tex(r"\rho", "#F87089")
# tex_waveq_final.set_color_by_tex(r"u", "#308167")