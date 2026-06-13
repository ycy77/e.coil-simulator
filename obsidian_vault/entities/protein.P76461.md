---
entity_id: "protein.P76461"
entity_type: "protein"
name: "atoB"
source_database: "UniProt"
source_id: "P76461"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atoB b2224 JW2218"
---

# atoB

`protein.P76461`

## Static

- Type: `protein`
- Source: `UniProt:P76461`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

Acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase) AtoB is one of two 3-ketoacyl-CoA thiolases in E. coli. While FADA-MONOMER FadA has broad substrate specificity, AtoB is strictly specific for acetoacetyl-CoA . Crystal structures of AtoB alone and in a complex with CoA have been solved; the structure can be described as a loosely interacting dimer of tight dimers . The gene for this study was cloned from E. coli BL21 (DE3), but the sequence is identical to that of the K-12 protein. AtoB expression is induced by growth on acetoacetate . AtoB is used for metabolic engineering of 1-butanol and medium-chain fuel production. AtoB: "acetoacetate"

## Biological Role

Catalyzes acetyl-CoA:acetyl-CoA C-acetyltransferase (reaction.R00238). Component of acetyl-CoA acetyltransferase (complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX).

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

Acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase)

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

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - via EC:2.3.1.9
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2224|gene.b2224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76461`
- `KEGG:ecj:JW2218;eco:b2224;ecoc:C3026_12430;`
- `GeneID:946727;`
- `GO:GO:0003985; GO:0005737; GO:0032991; GO:0042802; GO:0043442`
- `EC:2.3.1.9`

## Notes

Acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase)
