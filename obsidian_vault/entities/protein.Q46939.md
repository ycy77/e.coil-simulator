---
entity_id: "protein.Q46939"
entity_type: "protein"
name: "yqeF"
source_database: "UniProt"
source_id: "Q46939"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqeF b2844 JW5453"
---

# yqeF

`protein.Q46939`

## Static

- Type: `protein`
- Source: `UniProt:Q46939`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

Probable acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase) yqeF encodes a predicted acetyl-CoA acetyltransferase . Expression of YqeF together with FucO enables engineered reversal of the fatty acid β-oxidation cycle for production of butanol . yqeF is induced during a second phase of growth on mucus when genes for anaerobic respiration, ethanolamine and fucose degradation, and the TCA cycle are induced . yqeF was shown to be upregulated in glucose-limited chemostat cultures . Mutation of the three PhoB binding sites in the yqeF-yqeG intergenic region resulted in five-fold decreased expression of yqeF .

## Biological Role

Catalyzes acetyl-CoA:acetyl-CoA C-acetyltransferase (reaction.R00238).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

Probable acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase)

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - via EC:2.3.1.9

## Incoming Edges (1)

- `encodes` <-- [[gene.b2844|gene.b2844]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46939`
- `KEGG:ecj:JW5453;eco:b2844;ecoc:C3026_15615;`
- `GeneID:947324;`
- `GO:GO:0003985; GO:0003988; GO:0005737; GO:0071271`
- `EC:2.3.1.9`

## Notes

Probable acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase)
