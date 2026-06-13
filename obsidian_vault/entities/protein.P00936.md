---
entity_id: "protein.P00936"
entity_type: "protein"
name: "cyaA"
source_database: "UniProt"
source_id: "P00936"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyaA cya b3806 JW3778"
---

# cyaA

`protein.P00936`

## Static

- Type: `protein`
- Source: `UniProt:P00936`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the formation of the second messenger cAMP from ATP. Its transcript is probably degraded by endoribonuclease LS (rnlA), decreasing cAMP levels and the negative regulator Crp-cAMP, which then induces its own transcription again. Adenylate cyclase catalyzes the synthesis of cyclic AMP (cAMP) by an intramolecular transfer of the adenylyl group of ATP to the 3'-hydroxy group, releasing pyrophosphate; thus, CyaA helps regulate the cellular concentration of cAMP. cAMP is an important signaling molecule; the role of cAMP in regulating the production of metabolic enzymes was first summarized in . The absence of cAMP affects the expression of alternative carbon source uptake and degradation systems involved in central metabolism . Via binding to the CAP/CRP protein (see CPLX0-226), it participates in the regulation of transcription of many genes. Adenylate cyclase is present at very low levels of approximately 15 molecules/cell . Its rare UUG initiation codon, which was confirmed by N-terminal sequencing of the purified protein , limits the translation of cyaA . Polyamines stimulate synthesis of adenylate cyclase at the level of translation initiation . The regulation of adenylate cyclase has been studied for many years, but the results were often contradictory...

## Biological Role

Catalyzes ATP diphosphate-lyase (cyclizing; 3',5'-cyclic-AMP-forming) (reaction.R00089), GTP diphosphate-lyase (cyclizing; 3',5'-cyclic-GMP-forming) (reaction.R00434), ADENYLATECYC-RXN (reaction.ecocyc.ADENYLATECYC-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of the second messenger cAMP from ATP. Its transcript is probably degraded by endoribonuclease LS (rnlA), decreasing cAMP levels and the negative regulator Crp-cAMP, which then induces its own transcription again.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00089|reaction.R00089]] `KEGG` `database` - via EC:4.6.1.1
- `catalyzes` --> [[reaction.R00434|reaction.R00434]] `KEGG` `database` - via EC:4.6.1.1
- `catalyzes` --> [[reaction.ecocyc.ADENYLATECYC-RXN|reaction.ecocyc.ADENYLATECYC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3806|gene.b3806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00936`
- `KEGG:ecj:JW3778;eco:b3806;ecoc:C3026_20605;`
- `GeneID:947755;`
- `GO:GO:0004016; GO:0005524; GO:0005737; GO:0006171`
- `EC:4.6.1.1`

## Notes

Adenylate cyclase (EC 4.6.1.1) (ATP pyrophosphate-lyase) (Adenylyl cyclase)
