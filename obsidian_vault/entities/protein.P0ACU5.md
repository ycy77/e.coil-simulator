---
entity_id: "protein.P0ACU5"
entity_type: "protein"
name: "fabR"
source_database: "UniProt"
source_id: "P0ACU5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabR yijC b3963 JW3935"
---

# fabR

`protein.P0ACU5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACU5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Binds the promoter region of at least fabA and fabB, but probably not yqfA (PubMed:11160901, PubMed:19854834, PubMed:21276098). Represses the transcription of fabA and fabB, involved in unsaturated fatty acid (UFA) biosynthesis (PubMed:11859088). By controlling UFA production, FabR directly influences the physical properties of the membrane bilayer. {ECO:0000269|PubMed:11160901, ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098}. FabR, "Fatty acid biosynthesis Regulator," represses expression of the fabA and fabB genes, which are essential for the synthesis of monounsaturated fatty acids . FabR directly influences membrane lipid homeostasis . It is a unique example of a transcription factor exclusively regulating expression of type II fatty acid synthase enzymes . The FabR consensus sequence has been identified as a palindromic sequence with a length of 18 bp . DNA binding and repression require the binding of unsaturated acyl-ACP (acyl-acyl carrier protein) or acyl-CoA. Saturated acyl-ACP or acyl-CoA competes with the unsaturated fatty acids for binding to FabR but does not trigger DNA binding . Thus, FabR senses the ratio, rather than the absolute amount, of unsaturated and saturated fatty acids and adjusts expression of fabA and fabB to balance the composition of saturated and unsaturated acyl-ACP...

## Annotation

FUNCTION: Binds the promoter region of at least fabA and fabB, but probably not yqfA (PubMed:11160901, PubMed:19854834, PubMed:21276098). Represses the transcription of fabA and fabB, involved in unsaturated fatty acid (UFA) biosynthesis (PubMed:11859088). By controlling UFA production, FabR directly influences the physical properties of the membrane bilayer. {ECO:0000269|PubMed:11160901, ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098}.

## Outgoing Edges (2)

- `represses` --> [[gene.b0954|gene.b0954]] `RegulonDB` `C` - regulator=FabR; target=fabA; function=-
- `represses` --> [[gene.b2323|gene.b2323]] `RegulonDB` `C` - regulator=FabR; target=fabB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3963|gene.b3963]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACU5`
- `KEGG:ecj:JW3935;eco:b3963;`
- `GeneID:948460;`
- `GO:GO:0003677; GO:0003700; GO:0005737; GO:0006633; GO:0045717; GO:0045892`

## Notes

HTH-type transcriptional repressor FabR
