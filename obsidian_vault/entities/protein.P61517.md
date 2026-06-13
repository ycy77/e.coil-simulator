---
entity_id: "protein.P61517"
entity_type: "protein"
name: "can"
source_database: "UniProt"
source_id: "P61517"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "can cynT2 yadF b0126 JW0122"
---

# can

`protein.P61517`

## Static

- Type: `protein`
- Source: `UniProt:P61517`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Carbonic anhydrase 2 (EC 4.2.1.1) (Carbonate dehydratase 2) E. coli encodes two carbonic anhydrases, CynT (CARBODEHYDRAT-MONOMER) and Can (carbonic anhydrase 2). The enzymes belong to Clade A and Clade B of the β class of carbonic anhydrases, respectively . Carbonic anhydrase 2 is essential for growth at amospheric pCO2 . Enzymatic activity of carbonic anhydrase 2 is pH-dependent . Inhibition of Can activity by sulfonamides and various clinically used drugs has been investigated . Crystal structures of carbonic anhydrase 2 have been solved. The crystal structure data as well as size exclusion chromatography indicate that the protein exists as a homotetramer in solution . There is structural evidence for a noncatalytic binding site for bicarbonate . A can mutant does not grow under normal atmospheric conditions, but the mutant can grow under conditions with a high exogenous or endogenous supply of CO2. Expression of cynT suppresses phenotypes of a can mutant . A can cynT double mutant is only viable under high CO2 conditions . Expression of can is inversely proportional to the growth rate and does not depend on CO2 levels . Under anaerobiosis, FNR represses can gene expression, but it is not known if this regulation is direct or indirect . Carbonic anhydrase 2 belongs to a set of native E...

## Biological Role

Catalyzes carbonate hydro-lyase (carbon-dioxide-forming); (reaction.R00132). Component of carbonic anhydrase 2 (complex.ecocyc.CPLX0-7521).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Carbonic anhydrase 2 (EC 4.2.1.1) (Carbonate dehydratase 2)

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00132|reaction.R00132]] `KEGG` `database` - via EC:4.2.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7521|complex.ecocyc.CPLX0-7521]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0126|gene.b0126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P61517`
- `KEGG:ecj:JW0122;eco:b0126;ecoc:C3026_00535;`
- `GeneID:93777310;944832;`
- `GO:GO:0004089; GO:0005829; GO:0008270; GO:0015976; GO:0042802; GO:0051289`
- `EC:4.2.1.1`

## Notes

Carbonic anhydrase 2 (EC 4.2.1.1) (Carbonate dehydratase 2)
