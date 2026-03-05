from flask import Flask, render_template, request

app = Flask(__name__)

# ── Real data from powervision.co.zw ─────────────────────────────────────────

SERVICES = [
    {
        "id": "green-energy",
        "slug": "alternative-green-energy",
        "nav_label": "Alternative and Green Energy Solutions",
        "icon": "bi-sun",
        "title": "Alternative and Green Energy Solutions",
        "tagline": "Residential, Commercial and Industrial Solar Solutions",
        "description": (
            "Powervision has extensive experience and expertise in renewable energy solutions. "
            "We can design and install a system tailored to specific requirements, regardless of its scale. "
            "Whether it's a homeowner looking to reduce electricity bills, a business owner seeking a reliable "
            "and sustainable energy source, or an industrial facility requiring a high-powered solar solution, "
            "Powervision has the experience and resources to empower with clean and renewable energy. "
            "We are the authorised service centre for major international leading companies in the manufacture "
            "of high-quality inverters."
        ),
        "features": [
            "Residential, Commercial and Industrial solar solutions",
            "Registered dealers: Synsynk, Deye, Alpha Outback, Atess, Victron and Fronius Inverters",
            "Solar powered water pumping — Lorentz and Grundfos range",
            "Astro Energy (Chint) and Jinko PV modules above 500W",
            "Solar water heaters for domestic and industrial use",
            "Solar lighting — home, office, street, parking and security",
            "SCADA solutions and remote monitoring",
            "Various accessories including charge controllers",
        ],
        "products": [
            {
                "name": "Inverters",
                "detail": "Residential, Commercial and Industrial inverter systems ranging 1kW to several MW. Registered dealers for Synsynk, Deye, Alpha Outback, Atess, Victron and Fronius.",
            },
            {
                "name": "PV Modules",
                "detail": "Astro Energy (Chint) and Jinko range of PV modules ranging above 500W.",
            },
            {
                "name": "Solar Pumps",
                "detail": "Lorentz and Grundfos range of solar pumps, controllers and allied accessories.",
            },
            {
                "name": "Batteries",
                "detail": "Wide range of Grade A and B Lithium-ion batteries for LV and HV solutions. Registered dealer for WECO, Pylontech, FreedomWon and Sunsynk batteries.",
            },
        ],
    },
    {
        "id": "electrical",
        "slug": "electrical-installations",
        "nav_label": "Electrical Installations",
        "icon": "bi-lightning-charge",
        "title": "Electrical Installations",
        "tagline": "LV, MV and HT Power Line & Substation Installations",
        "description": (
            "We undertake electrical installations for all the equipment that we supply, and in addition "
            "we also undertake electrical repairs and maintenance on all other equipment. "
            "We have experience and have commissioned projects in the LV and HT power line and substation installations. "
            "Our scope covers generation and approval of technical specifications, statement of works, "
            "bills of quantities, cable schedules, design calculations for cable selection, lighting, "
            "and electrical distribution, as well as electrical schematic and connection diagrams for "
            "distribution, control, interfacing and interlocking."
        ),
        "features": [
            "LV and HT power line and substation installations",
            "Electrical repairs and maintenance",
            "Technical specifications and statement of works",
            "Bills of quantities and cable schedules",
            "Design calculations for cable selection, lighting and distribution",
            "Electrical schematic and connection diagrams",
            "Distribution, control, interfacing and interlocking diagrams",
            "Industrial, commercial and domestic electrical fit-outs",
        ],
        "products": [],
    },
    {
        "id": "backup-power",
        "slug": "backup-standby-power",
        "nav_label": "Back-Up and Standby Power",
        "icon": "bi-battery-charging",
        "title": "Back-Up and Standby Power",
        "tagline": "UPS, Generators and Battery Systems",
        "description": (
            "Keep your critical systems running smoothly during outages, ensuring seamless operation "
            "and protecting equipment from damaging power surges. Powervision offers design, installation "
            "and maintenance of diesel generators, as well as a full range of UPS solutions. "
            "Our hybrid systems, incorporating Outback Power products, have advanced communication and "
            "remote monitoring functionality, making them the best choice for remote base stations. "
            "Our solutions make it possible to connect the inverter to the generator, enabling the "
            "inverter to start the generator as and when needed, saving on fuel."
        ),
        "features": [
            "Design, installation and maintenance of diesel generators",
            "American Power Company (Schneider Electric) UPS from 500VA to 200kVA",
            "Tripplite UPS solutions",
            "Power protection equipment including surge protectors",
            "Grade A and B Lithium-ion batteries for LV and HV solutions",
            "Registered dealer: WECO, Pylontech, FreedomWon and Sunsynk batteries",
            "Batteries for backup power: CSB, Panasonic and Yuasa",
            "Automatic transfer switches and generator-inverter integration",
        ],
        "products": [
            {
                "name": "UPS Systems",
                "detail": "American Power Company (Schneider Electric) UPS from 500VA to 200kVA. Power protection equipment including surge protectors. Tripplite UPS solutions.",
            },
            {
                "name": "Batteries",
                "detail": "Wide range of Grade A and B Lithium-ion batteries for LV and HV solutions. Registered dealer for WECO, Pylontech, FreedomWon and Sunsynk. Also CSB, Panasonic and Yuasa for backup power applications.",
            },
            {
                "name": "Generators",
                "detail": "Design, installation and maintenance of diesel generators with inverter integration for fuel-efficient automated operation.",
            },
        ],
    },
    {
        "id": "protection",
        "slug": "power-system-protection",
        "nav_label": "Power System Protection",
        "icon": "bi-shield-check",
        "title": "Power System Protection",
        "tagline": "Surge Protection, Voltage Regulation and Lightning Protection",
        "description": (
            "Power disruptions like blackouts, voltage fluctuations, and lightning strikes can cripple "
            "operations and damage expensive equipment. Powervision safeguards your business with a "
            "comprehensive suite of power protection solutions. "
            "For areas prone to voltage fluctuations, Powervision offers premium surge protection devices "
            "and voltage regulators. Our Ortea, Delta and Neopower range, with their impressive warranty, "
            "guarantees quality and consistent power for your facilities. "
            "We also offer Constant Voltage Transformers, Stabilised Power Supplies, and Phase Angle Relays "
            "to safeguard equipment from even the most damaging power surges, including those that threaten "
            "borehole pumps."
        ),
        "features": [
            "Surge protection for power supply systems — AC and DC",
            "Surge protection for IT systems",
            "Lightning and earthing protection",
            "Ortea, Delta and Neopower voltage regulators",
            "Constant Voltage Transformers",
            "Stabilised Power Supplies",
            "Phase Angle Relays",
            "Protection for borehole pumps and sensitive equipment",
        ],
        "products": [
            {
                "name": "Surge Protection",
                "detail": "Surge protection for power supply systems (AC and DC), IT systems, and lightning and earthing protection.",
            },
            {
                "name": "Voltage Regulators",
                "detail": "Ortea, Delta and Neopower range with impressive warranty for consistent, quality power.",
            },
        ],
    },
    {
        "id": "value-added",
        "slug": "value-added-services",
        "nav_label": "Value Added Services",
        "icon": "bi-tools",
        "title": "Value Added Services",
        "tagline": "Consultative, Audit and Project Management Services",
        "description": (
            "Powervision services extend to offering consultative services including site audits, "
            "power and energy audits for electrical installations and system enhancements. "
            "We offer safety and compliance auditing of all electrical HV/MV/LV and control and "
            "instrumentation installations, analysis of planned electrical needs during the design phase, "
            "and project management and planning for renewable energy projects, electrical installations, "
            "electrical reticulation and backup power system installations. "
            "Powervision also offers premium solutions for integrating the various power technologies "
            "to ensure optimal and usable solutions."
        ),
        "features": [
            "Site audits, power and energy audits",
            "Safety and compliance auditing — HV/MV/LV and C&I installations",
            "Analysis of planned electrical needs during design phase",
            "Project management and planning for renewable energy projects",
            "Electrical reticulation and backup power system planning",
            "Technology integration for optimal hybrid solutions",
            "Consultative services for system enhancements",
            "Generation and approval of technical specifications",
        ],
        "products": [],
    },
    {
        "id": "products",
        "slug": "products",
        "nav_label": "Products",
        "icon": "bi-box-seam",
        "title": "Products",
        "tagline": "Quality-Assured Electrical and Solar Products",
        "description": (
            "Powervision supplies a wide range of quality-assured electrical and solar products from "
            "leading global manufacturers. All products are sourced to meet Zimbabwe and international "
            "standards and are backed by our technical support team. We are registered dealers and "
            "authorised service centres for several major international brands."
        ),
        "features": [
            "Inverters: Synsynk, Deye, Alpha Outback, Atess, Victron, Fronius (1kW to several MW)",
            "UPS: Schneider Electric (APC) 500VA–200kVA, Tripplite",
            "Batteries: WECO, Pylontech, FreedomWon, Sunsynk, CSB, Panasonic, Yuasa",
            "PV Modules: Astro Energy (Chint), Jinko — above 500W",
            "Solar Pumps: Lorentz and Grundfos range",
            "Surge Protection: Ortea, Delta, Neopower",
            "Charge controllers, remote monitoring and SCADA solutions",
            "Cables, conduits, switchgear and allied accessories",
        ],
        "products": [],
    },
]

STATS = [
    {"value": "20+", "label": "Years in Business"},
    {"value": "50+", "label": "Companies Served"},
    {"value": "150+", "label": "Projects Tackled"},
]

CONTACT = {
    "email": "powerhelp@power.co.zw",
    "phone": "+263 8677 005125",
    "address": "P.O. Box 26, Amby Drive, Greendale, Harare, Zimbabwe",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
}


@app.route("/")
def index():
    return render_template("index.html", stats=STATS, services=SERVICES, contact=CONTACT)


@app.route("/about")
def about():
    return render_template("about.html", stats=STATS, contact=CONTACT)


@app.route("/the-team")
def team():
    return render_template("team.html", contact=CONTACT)


@app.route("/products-services")
def services():
    return render_template("services.html", services=SERVICES, contact=CONTACT)


@app.route("/products-services/<slug>")
def service_detail(slug):
    service = next((s for s in SERVICES if s["slug"] == slug), None)
    if not service:
        return "Not found", 404
    return render_template("service_detail_page.html", service=service, contact=CONTACT)


@app.route("/contact")
def contact():
    return render_template("contact.html", contact=CONTACT)


# ── HTMX partials ──────────────────────────────────────────────────────────────

@app.route("/htmx/services/<service_id>")
def htmx_service_detail(service_id):
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if not service:
        return "", 404
    return render_template("partials/service_detail.html", service=service)


@app.route("/htmx/quote", methods=["POST"])
def htmx_quote():
    name = request.form.get("name", "")
    service = request.form.get("service", "")
    return render_template("partials/quote_success.html", name=name, service=service)


if __name__ == "__main__":
    app.run()
