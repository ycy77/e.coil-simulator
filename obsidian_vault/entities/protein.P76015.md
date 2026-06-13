---
entity_id: "protein.P76015"
entity_type: "protein"
name: "dhaK"
source_database: "UniProt"
source_id: "P76015"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dhaK ycgT b1200 JW5187"
---

# dhaK

`protein.P76015`

## Static

- Type: `protein`
- Source: `UniProt:P76015`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dihydroxyacetone binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone via a phosphoryl group transfer from DhaL-ATP (PubMed:11350937, PubMed:15476397). Binds covalently dihydroxyacetone in hemiaminal linkage (PubMed:15476397). DhaK also acts as corepressor of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:24440518). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:24440518). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:24440518). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15476397, ECO:0000269|PubMed:24440518}. DhaK is similar to the N-terminal half of the ATP-dependent dihydroxyacetone kinase of Citrobacter freundii and eukaryotes . Crystal structures of apo-DhaK, DhaK in complex with dihydroxyacetone (DHA) as well as glyceraldehyde or DHA-phosphate , and the DhaK-DhaL complex have been solved. DhaK is a homodimer in the crystal structure; DHA is bound in a hemiaminal linkage to the Nε2 of His218 in the active site . A H218A mutant lacks kinase activity ; the His56 residue is involved in formation of the DHA-His218 hemiaminal bond . Covalent binding of DHA to His218 orients DHA for subsequent phosphoryl transfer...

## Biological Role

Catalyzes phosphoenolpyruvate:glycerone phosphotransferase (reaction.R01012). Component of dihydroxyacetone kinase (complex.ecocyc.CPLX0-2081).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Dihydroxyacetone binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone via a phosphoryl group transfer from DhaL-ATP (PubMed:11350937, PubMed:15476397). Binds covalently dihydroxyacetone in hemiaminal linkage (PubMed:15476397). DhaK also acts as corepressor of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:24440518). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:24440518). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:24440518). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15476397, ECO:0000269|PubMed:24440518}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - via EC:2.7.1.121
- `is_component_of` --> [[complex.ecocyc.CPLX0-2081|complex.ecocyc.CPLX0-2081]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1200|gene.b1200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76015`
- `KEGG:ecj:JW5187;eco:b1200;ecoc:C3026_07055;`
- `GeneID:945747;`
- `GO:GO:0004371; GO:0005829; GO:0006974; GO:0019563; GO:0042182; GO:0042802; GO:0042803; GO:0046365; GO:0046835; GO:0047324; GO:0061610; GO:1990234`
- `EC:2.7.1.121`

## Notes

PEP-dependent dihydroxyacetone kinase, dihydroxyacetone-binding subunit DhaK (EC 2.7.1.121)
