---
entity_id: "complex.ecocyc.PYRUVATEDEH-CPLX"
entity_type: "complex"
name: "pyruvate dehydrogenase"
source_database: "EcoCyc"
source_id: "PYRUVATEDEH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyruvate dehydrogenase

`complex.ecocyc.PYRUVATEDEH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PYRUVATEDEH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.E1P-CPLX|complex.ecocyc.E1P-CPLX]], [[protein.P06959|protein.P06959]], [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]]

## Enriched Summary

Pyruvate dehydrogenase is one of the most complicated enzyme systems known. The self-assembling complex is composed of multiple copies of three enzymes: E1, E2 and E3, in stoichiometry of 24:24:12, respectively (12 AceE dimers, a 24-subunit AceF core, and 6 LpdA dimers) . AceF, the "E2" or "core" component of the pyruvate dehydrogenase multienzyme complex, assembles into a 24-subunit cube . The E1 dimers of the pyruvate dehydrogenase multienzyme complex catalyze acetylation of the lipoate moieties that are attached to the E2 subunits . The E2 subunits (AceF) also exhibit transacetylation . The structure of the pyruvate dehydrogenase multienzyme complex and the spatial distribution of the E2 lipoyl moieties have been studied by scanning transmission electron microscopy . Electron cryotomography showed that the E1 and E3 subunits are flexibly tethered to the E2 core . The E3 component is shared with 2-oxoglutarate dehydrogenase and glycine cleavage multi-enzyme complexes. E1 and E2 differ slightly between 2-oxoglutarate and pyruvate complexes, and are designated (o) and (p) to distinguish them. Substrate is channeled through the catalytic reactions by attachment in thioester linkage to lipoyl groups via so-called 'swinging arm', carrying substrate molecules to successive active sites...

## Biological Role

Catalyzes PYRUVDEH-RXN (reaction.ecocyc.PYRUVDEH-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305), (R)-Lipoate (molecule.C16241).

## Annotation

Pyruvate dehydrogenase is one of the most complicated enzyme systems known. The self-assembling complex is composed of multiple copies of three enzymes: E1, E2 and E3, in stoichiometry of 24:24:12, respectively (12 AceE dimers, a 24-subunit AceF core, and 6 LpdA dimers) . AceF, the "E2" or "core" component of the pyruvate dehydrogenase multienzyme complex, assembles into a 24-subunit cube . The E1 dimers of the pyruvate dehydrogenase multienzyme complex catalyze acetylation of the lipoate moieties that are attached to the E2 subunits . The E2 subunits (AceF) also exhibit transacetylation . The structure of the pyruvate dehydrogenase multienzyme complex and the spatial distribution of the E2 lipoyl moieties have been studied by scanning transmission electron microscopy . Electron cryotomography showed that the E1 and E3 subunits are flexibly tethered to the E2 core . The E3 component is shared with 2-oxoglutarate dehydrogenase and glycine cleavage multi-enzyme complexes. E1 and E2 differ slightly between 2-oxoglutarate and pyruvate complexes, and are designated (o) and (p) to distinguish them. Substrate is channeled through the catalytic reactions by attachment in thioester linkage to lipoyl groups via so-called 'swinging arm', carrying substrate molecules to successive active sites . The reaction catalyzed by the pyruvate dehydrogenase multienzyme complex is the gateway to the TCA cycle, producing acetylCoA for the first reaction. In animals, the reaction is regulated by phosphorylation of the E1 component, but not in E. coli .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (9)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.E1P-CPLX|complex.ecocyc.E1P-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=12
- `is_component_of` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P06959|protein.P06959]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24
- `is_component_of` <-- [[protein.P0A9P0|protein.P0A9P0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P0AFG8|protein.P0AFG8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=24

## External IDs

- `EcoCyc:PYRUVATEDEH-CPLX`

## Notes

12*complex.ecocyc.E1P-CPLX|24*protein.P06959|6*complex.ecocyc.E3-CPLX
