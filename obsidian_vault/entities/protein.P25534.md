---
entity_id: "protein.P25534"
entity_type: "protein"
name: "ubiH"
source_database: "UniProt"
source_id: "P25534"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiH visB b2907 JW2875"
---

# ubiH

`protein.P25534`

## Static

- Type: `protein`
- Source: `UniProt:P25534`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: Is likely an oxygenase that introduces the hydroxyl group at carbon four of 2-octaprenyl-6-methoxyphenol resulting in the formation of 2-octaprenyl-6-methoxy-1,4-benzoquinol. {ECO:0000269|PubMed:4572721}. ubiH is thought to encode 2-octaprenyl-6-methoxyphenol 4-hydroxylase, one of the aerobic hydroxylases in the ubiquinone biosynthesis pathway. No direct biochemical evidence for the enzymatic activity of UbiH exists to date. UbiH is a component of the Ubi complex metabolon . UbiH predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol. UbiH is predicted to contain FAD . Mutants in ubiH accumulate 2-octaprenyl-6-methoxyphenol ; accumulation of this compound may be the cause of the visible light sensitive phenotype of ubiH mutants . ubiH mutants are unable to grow on succinate or glycerol as the sole source of carbon. Inactivation of ubiH results in dependence on an intact RecA . ubiH, ubiF, ubiX, ubiG, and ubiE mutants from the Keio K-12 mutant collection showed elevated resistance to the broad-spectrum antibiotic D-cycloserine (DCS) when grown in complex media, suggesting that they may be involved in DCS sensitivity . ubiH belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12...

## Biological Role

Catalyzes 2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN (reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN). Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Is likely an oxygenase that introduces the hydroxyl group at carbon four of 2-octaprenyl-6-methoxyphenol resulting in the formation of 2-octaprenyl-6-methoxy-1,4-benzoquinol. {ECO:0000269|PubMed:4572721}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2907|gene.b2907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25534`
- `KEGG:ecj:JW2875;eco:b2907;ecoc:C3026_15935;`
- `GeneID:947388;`
- `GO:GO:0005737; GO:0006744; GO:0006979; GO:0008681; GO:0009416; GO:0071949; GO:0110142`
- `EC:1.14.13.-`

## Notes

2-octaprenyl-6-methoxyphenol hydroxylase (EC 1.14.13.-)
