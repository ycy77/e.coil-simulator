---
entity_id: "protein.P25535"
entity_type: "protein"
name: "ubiI"
source_database: "UniProt"
source_id: "P25535"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiI visC b2906 JW2874"
---

# ubiI

`protein.P25535`

## Static

- Type: `protein`
- Source: `UniProt:P25535`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: FAD-dependent monooxygenase required for the aerobic hydroxylation of 2-octaprenylphenol to 2-octaprenyl-6-hydroxy-phenol, the first hydroxylation step in coenzyme Q (ubiquinone) biosynthesis. {ECO:0000269|PubMed:23709220}. UbiI is a component of the Ubi complex metabolon . UbiI functions in the hydroxylation of the C5 position during the aerobic biosynthesis of ubiquinone-8. UbiI predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . Purified UbiI is unstable; an inactive truncated form was isolated and behaves like a tetramer in solution. The crystal structure of this protein has been solved at 2.0 Å resolution. Point mutants in the predicted FAD binding site do not complement a ΔubiI mutant . Deletion of ubiI (visC) has no effect on photosensitivity or aerobic respiration ; however, a ubiI mutant strain contains only 7% of wild type levels of ubiquinone-8 and accumulates 3-octaprenyl-4-hydroxyphenol (4-HP8) . The residual C5 hydroxylase activity appears to be provided by UbiF . A ΔubiIΔubiK double mutant produces no detectable ubiquinone and in contrast to the single mutants, has a significant growth defect when grown aerobically on rich medium and does not grow on the non-fermentable carbon sources oleate, acetate, and succinate...

## Biological Role

Catalyzes 2-OCTAPRENYLPHENOL-HYDROX-RXN (reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN). Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: FAD-dependent monooxygenase required for the aerobic hydroxylation of 2-octaprenylphenol to 2-octaprenyl-6-hydroxy-phenol, the first hydroxylation step in coenzyme Q (ubiquinone) biosynthesis. {ECO:0000269|PubMed:23709220}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2906|gene.b2906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25535`
- `KEGG:ecj:JW2874;eco:b2906;ecoc:C3026_15930;`
- `GeneID:947389;`
- `GO:GO:0005737; GO:0006744; GO:0019168; GO:0071949; GO:0110142`
- `EC:1.14.13.240`

## Notes

2-octaprenylphenol hydroxylase (EC 1.14.13.240) (2-polyprenylphenol 6-hydroxylase)
