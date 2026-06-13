---
entity_id: "complex.ecocyc.ABC-9-CPLX"
entity_type: "complex"
name: "ferric citrate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-9-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "iron dicitrate ABC transporter"
  - "ferric dicitrate ABC transporter"
---

# ferric citrate ABC transporter

`complex.ecocyc.ABC-9-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-9-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P15031|protein.P15031]], [[protein.P15030|protein.P15030]], [[protein.P15029|protein.P15029]], [[protein.P15028|protein.P15028]]

## Enriched Summary

E. coli K-12 contains a citrate dependent iron uptake system consisting of an inner membrane transporter, FecBCDE and an outer membrane, TonB dependent receptor EG10286-MONOMER "FecA". The system is induced by exogenous ferric citrate when intracellular iron is limiting FecBCDE is a member of the ATP binding cassette (ABC) superfamily of transporters . FecB is the periplasmic binding protein, FecC and FecD are the integral membrane proteins and FecE is the predicted ATP-binding protein . The exact species transported by FecBCDE seems unclear: early studies using labeled Fe(III) and labeled citrate suggest that only iron and not the iron complex enters the cytoplasm ; states that Fe(III) is transported into the periplasm (by FecA) as a diferric dicitrate complex and across the cytoplasmic membrane probably as Fe(III). Alternatively, if ferric dicitrate (or diferric dicitrate) is transported then iron may be released from the complex through the action of the intracellular ferric siderophore reductase, G7593-MONOMER "YqjH" . The fec transport genes (fecABCDE) form an operon in E. coli K-12 . Under iron-replete conditions fecABCDE transcription is repressed by Fe2+-Fur; under iron limiting conditions and in the presence of exogenous iron citrate, transcription is initiated by PD00440 "σ19" (FecI) containing RNA polymerase via a FecAR signaling cascade (reviewed by )...

## Biological Role

Catalyzes ABC-9-RXN (reaction.ecocyc.ABC-9-RXN). Transports Fe(III)dicitrate (molecule.C06229), hν (molecule.ecocyc.Light).

## Annotation

E. coli K-12 contains a citrate dependent iron uptake system consisting of an inner membrane transporter, FecBCDE and an outer membrane, TonB dependent receptor EG10286-MONOMER "FecA". The system is induced by exogenous ferric citrate when intracellular iron is limiting FecBCDE is a member of the ATP binding cassette (ABC) superfamily of transporters . FecB is the periplasmic binding protein, FecC and FecD are the integral membrane proteins and FecE is the predicted ATP-binding protein . The exact species transported by FecBCDE seems unclear: early studies using labeled Fe(III) and labeled citrate suggest that only iron and not the iron complex enters the cytoplasm ; states that Fe(III) is transported into the periplasm (by FecA) as a diferric dicitrate complex and across the cytoplasmic membrane probably as Fe(III). Alternatively, if ferric dicitrate (or diferric dicitrate) is transported then iron may be released from the complex through the action of the intracellular ferric siderophore reductase, G7593-MONOMER "YqjH" . The fec transport genes (fecABCDE) form an operon in E. coli K-12 . Under iron-replete conditions fecABCDE transcription is repressed by Fe2+-Fur; under iron limiting conditions and in the presence of exogenous iron citrate, transcription is initiated by PD00440 "σ19" (FecI) containing RNA polymerase via a FecAR signaling cascade (reviewed by ). Related reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-9-RXN|reaction.ecocyc.ABC-9-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P15028|protein.P15028]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P15029|protein.P15029]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P15030|protein.P15030]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P15031|protein.P15031]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-9-CPLX`
- `QSPROTEOME:QS00181543`

## Notes

2*protein.P15031|1*protein.P15030|1*protein.P15029|1*protein.P15028
