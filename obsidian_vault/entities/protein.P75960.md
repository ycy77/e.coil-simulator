---
entity_id: "protein.P75960"
entity_type: "protein"
name: "cobB"
source_database: "UniProt"
source_id: "P75960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01121}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cobB ycfY b1120 JW1106"
---

# cobB

`protein.P75960`

## Static

- Type: `protein`
- Source: `UniProt:P75960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01121}.

## Enriched Summary

FUNCTION: NAD-dependent lysine deacetylase that specifically removes acetyl groups on target proteins. Also acts as a protein-lysine deacylase by mediating protein desuccinylation and de-2-hydroxyisobutyrylation. Modulates the activities of several proteins which are inactive in their acylated form. Activates the enzyme acetyl-CoA synthetase (acs) by deacetylating 'Lys-609' in the inactive, acetylated form of the enzyme. May also modulate the activity of other propionyl-adenosine monophosphate (AMP)-forming enzymes. {ECO:0000255|HAMAP-Rule:MF_01121, ECO:0000269|PubMed:10811920, ECO:0000269|PubMed:15019790, ECO:0000269|PubMed:24176774, ECO:0000269|PubMed:30274179, ECO:0000269|PubMed:31328167}. The shorter CobB-S isoform is produced by translation initiation at an alternative start codon in a transcript that is apparently created by use of an alternative promoter . The N-terminal domain which is only present in the G6577-MONOMER CobB-L isoform appears to be required for dimerization .

## Biological Role

Component of protein-lysine deacetylase/desuccinylase/delipoylase (complex.ecocyc.CPLX0-8550).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NAD-dependent lysine deacetylase that specifically removes acetyl groups on target proteins. Also acts as a protein-lysine deacylase by mediating protein desuccinylation and de-2-hydroxyisobutyrylation. Modulates the activities of several proteins which are inactive in their acylated form. Activates the enzyme acetyl-CoA synthetase (acs) by deacetylating 'Lys-609' in the inactive, acetylated form of the enzyme. May also modulate the activity of other propionyl-adenosine monophosphate (AMP)-forming enzymes. {ECO:0000255|HAMAP-Rule:MF_01121, ECO:0000269|PubMed:10811920, ECO:0000269|PubMed:15019790, ECO:0000269|PubMed:24176774, ECO:0000269|PubMed:30274179, ECO:0000269|PubMed:31328167}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8550|complex.ecocyc.CPLX0-8550]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1120|gene.b1120]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75960`
- `KEGG:ecj:JW1106;eco:b1120;ecoc:C3026_06745;`
- `GeneID:75203706;945687;`
- `GO:GO:0003950; GO:0005737; GO:0006935; GO:0008270; GO:0034979; GO:0035438; GO:0036054; GO:0036055; GO:0042803; GO:0051607; GO:0061690; GO:0070403; GO:0160013`
- `EC:2.3.1.286`

## Notes

NAD-dependent protein deacylase (EC 2.3.1.286) (Regulatory protein SIR2 homolog)
