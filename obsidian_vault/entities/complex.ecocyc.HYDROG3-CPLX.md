---
entity_id: "complex.ecocyc.HYDROG3-CPLX"
entity_type: "complex"
name: "hydrogenase 3"
source_database: "EcoCyc"
source_id: "HYDROG3-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# hydrogenase 3

`complex.ecocyc.HYDROG3-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HYDROG3-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16430|protein.P16430]], [[protein.P16429|protein.P16429]], [[protein.P16432|protein.P16432]], [[protein.P16433|protein.P16433]], [[protein.P0AAK1|protein.P0AAK1]], [[protein.P16431|protein.P16431]]

## Enriched Summary

Microbial hydrogenases catalyse the reversible reduction of protons to molecular hydrogen. E. coli hydrogenase 3, encoded by the hyc genes (hycB, hycC, hycD, hycE, hycF and hycG), is a multisubunit enzyme that forms part of the FHLMULTI-CPLX "formate hydrogenlyase (FHL) complex" responsible for the fermentative or anaerobic oxidation of formic acid to carbon dioxide and molecular hydrogen . Hydrogenase 3 functions primarily in the production of H2 and is important for H2 production at acidic pH . Hydrogen uptake in a strain lacking hydrogenase 1 and hydrogenase 2 is further reduced by the incorporation of a hycE mutation, suggesting that hydrogenase 3 can also function in hydrogen uptake . Hydrogenase 3 shows a high tolerance to product (H2) inhibition . Hydrogenase 3 is a membrane associated H2 evolving respiratory [NiFe] hydrogenase. It contains the large (HycE) and small (HycG) subunits that are characteristic of 'standard' NiFe hydrogenases plus two additional hydrophilic subunits (HycB and HycF) and two inner membrane subunits (HycC and HycD). Fe-S prosthetic groups located in the hydrophilic part of the complex may form the electron transport pathway (reviews: )...

## Biological Role

Catalyzes hydrogenase (reaction.ecocyc.HYDROG-RXN). Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX).

## Annotation

Microbial hydrogenases catalyse the reversible reduction of protons to molecular hydrogen. E. coli hydrogenase 3, encoded by the hyc genes (hycB, hycC, hycD, hycE, hycF and hycG), is a multisubunit enzyme that forms part of the FHLMULTI-CPLX "formate hydrogenlyase (FHL) complex" responsible for the fermentative or anaerobic oxidation of formic acid to carbon dioxide and molecular hydrogen . Hydrogenase 3 functions primarily in the production of H2 and is important for H2 production at acidic pH . Hydrogen uptake in a strain lacking hydrogenase 1 and hydrogenase 2 is further reduced by the incorporation of a hycE mutation, suggesting that hydrogenase 3 can also function in hydrogen uptake . Hydrogenase 3 shows a high tolerance to product (H2) inhibition . Hydrogenase 3 is a membrane associated H2 evolving respiratory [NiFe] hydrogenase. It contains the large (HycE) and small (HycG) subunits that are characteristic of 'standard' NiFe hydrogenases plus two additional hydrophilic subunits (HycB and HycF) and two inner membrane subunits (HycC and HycD). Fe-S prosthetic groups located in the hydrophilic part of the complex may form the electron transport pathway (reviews: ). Sequence similarity between the genes encoding hydrogenase 3 and those encoding subunits that form the core of energy conserving NADH:quinone oxidoreductases have been reported and an evolutionary relationship between the two has been proposed ; subsequent research is consistent with this proposal . Strains with insertion mutations of genes within the hyc operon are defective for hydrogenase activity . The hyc operon is regulated coordinately with the structural gene for FORMATEDEHYDROGH-MONOMER "formate dehydrogenase H". Expression is repressed by oxygen and by nitrate and induced by formate under fermen

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.HYDROG-RXN|reaction.ecocyc.HYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (6)

- `is_component_of` <-- [[protein.P0AAK1|protein.P0AAK1]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16429|protein.P16429]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16430|protein.P16430]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16431|protein.P16431]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16432|protein.P16432]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16433|protein.P16433]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:HYDROG3-CPLX`
- `PDB:7Z0T`
- `PDB:7Z0S`
- `QSPROTEOME:QS00196153`

## Notes

protein.P16430|protein.P16429|protein.P16432|protein.P16433|protein.P0AAK1|protein.P16431
