---
entity_id: "protein.P76458"
entity_type: "protein"
name: "atoD"
source_database: "UniProt"
source_id: "P76458"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1103739}. Note=Membrane associated. {ECO:0000269|PubMed:1103739}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atoD b2221 JW2215"
---

# atoD

`protein.P76458`

## Static

- Type: `protein`
- Source: `UniProt:P76458`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1103739}. Note=Membrane associated. {ECO:0000269|PubMed:1103739}.

## Enriched Summary

FUNCTION: Coenzyme A transferase which is involved in short-chain fatty acid degradation and catalyzes the activation of short-chain fatty acids to their respective CoA thiolesters (PubMed:1103739, PubMed:3025185). During acetoacetate degradation, catalyzes the transfer of CoA from acetyl-CoA to acetoacetate by a mechanism involving a covalent enzyme-CoA compound as a reaction intermediate (PubMed:1103741). Utilizes a variety of short chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates (PubMed:1103739). {ECO:0000269|PubMed:1103739, ECO:0000269|PubMed:1103741, ECO:0000269|PubMed:3025185}. Based on sequence similarity, AtoD is predicted to be an acetate CoA-transferase . AtoD: "acetoacetate"

## Biological Role

Catalyzes acyl-CoA:acetate CoA-transferase (reaction.R00393). Component of acetoacetyl-CoA transferase (complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX), cetyl-CoA:acetoacetyl-CoA transferase subunit α dimer (complex.ecocyc.ATOD-CPLX).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Coenzyme A transferase which is involved in short-chain fatty acid degradation and catalyzes the activation of short-chain fatty acids to their respective CoA thiolesters (PubMed:1103739, PubMed:3025185). During acetoacetate degradation, catalyzes the transfer of CoA from acetyl-CoA to acetoacetate by a mechanism involving a covalent enzyme-CoA compound as a reaction intermediate (PubMed:1103741). Utilizes a variety of short chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates (PubMed:1103739). {ECO:0000269|PubMed:1103739, ECO:0000269|PubMed:1103741, ECO:0000269|PubMed:3025185}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00393|reaction.R00393]] `KEGG` `database` - via EC:2.8.3.8
- `is_component_of` --> [[complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX|complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ATOD-CPLX|complex.ecocyc.ATOD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2221|gene.b2221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76458`
- `KEGG:ecj:JW2215;eco:b2221;ecoc:C3026_12415;`
- `GeneID:93774955;947525;`
- `GO:GO:0005737; GO:0008410; GO:0008775; GO:0046459; GO:0047371`
- `EC:2.8.3.8`

## Notes

Acetate CoA-transferase subunit alpha (EC 2.8.3.8) (Acetoacetyl-CoA transferase subunit alpha) (AA-CoA transferase subunit alpha) (Acetyl-CoA:acetoacetyl-CoA transferase subunit alpha)
