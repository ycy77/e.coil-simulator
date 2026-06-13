---
entity_id: "protein.P76014"
entity_type: "protein"
name: "dhaL"
source_database: "UniProt"
source_id: "P76014"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dhaL ycgS b1199 JW5186"
---

# dhaL

`protein.P76014`

## Static

- Type: `protein`
- Source: `UniProt:P76014`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: ADP-binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone (PubMed:11350937). DhaL-ADP is converted to DhaL-ATP via a phosphoryl group transfer from DhaM and transmits it to dihydroxyacetone bound to DhaK (PubMed:11350937). DhaL also acts as coactivator of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:15616579). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:15616579). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:15616579). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15616579}. DhaL is similar to the C-terminal half of the ATP-dependent dihydroxyacetone kinase of Citrobacter freundii and eukaryotes . DhaL contains bound ADP which is transiently phosphorylated as a cofactor in the kinase reaction . Crystal structures of the DhaL-ADP complex and the DhaK-DhaL complex have been solved. The proximity of the DHA-binding site in DhaK and the ADP/ATP-binding site in DhaL is consistent with a direct transfer of the γ-phosphate from ATP to the γ-hydroxyl group of DHA . ADP-bound DhaL is a coactivator of G6628-MONOMER DhaR, the transcription factor that controls expression of the dhaKLM operon...

## Biological Role

Catalyzes phosphoenolpyruvate:glycerone phosphotransferase (reaction.R01012). Component of dihydroxyacetone kinase (complex.ecocyc.CPLX0-2081).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: ADP-binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone (PubMed:11350937). DhaL-ADP is converted to DhaL-ATP via a phosphoryl group transfer from DhaM and transmits it to dihydroxyacetone bound to DhaK (PubMed:11350937). DhaL also acts as coactivator of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:15616579). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:15616579). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:15616579). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15616579}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - via EC:2.7.1.121
- `is_component_of` --> [[complex.ecocyc.CPLX0-2081|complex.ecocyc.CPLX0-2081]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1199|gene.b1199]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76014`
- `KEGG:ecj:JW5186;eco:b1199;ecoc:C3026_07050;`
- `GeneID:945748;`
- `GO:GO:0000287; GO:0004371; GO:0005524; GO:0005829; GO:0019563; GO:0043531; GO:0046835; GO:0047324; GO:1990234`
- `EC:2.7.1.121`

## Notes

PEP-dependent dihydroxyacetone kinase, ADP-binding subunit DhaL (EC 2.7.1.121)
