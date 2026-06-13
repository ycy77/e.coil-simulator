---
entity_id: "gene.b1850"
entity_type: "gene"
name: "eda"
source_database: "NCBI RefSeq"
source_id: "gene-b1850"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1850"
  - "eda"
---

# eda

`gene.b1850`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1850`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eda (gene.b1850) is a gene entity. It encodes eda (protein.P0A955). Encoded protein function: FUNCTION: Involved in the degradation of glucose via the Entner-Doudoroff pathway (PubMed:15659677, PubMed:1624451). Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogluconate (KDPG) to pyruvate and D-glyceraldehyde-3-phosphate (PubMed:11342129, PubMed:17962400, PubMed:17981470). In vitro, can also catalyze the cleavage of 2-keto-4-hydroxy-4-(2'-pyridyl)butyrate (KHPB), 2-keto-3-deoxy-6-phosphogalactonate (KDPGal), and of the substrate analogs 2-keto-3-deoxy-gluconate (KDG) and 2-keto-4-hydroxyoctonate (KHO) (PubMed:17962400). Can accept some nucleophiles other than pyruvate, including 2-oxobutanoate, phenylpyruvate and fluorobutanoate (PubMed:17981470). In addition to its KDPG aldolase activity, catalyzes the reversible cleavage of 2-keto-4-hydroxyglutarate (KHG) to glyoxylate and pyruvate (PubMed:1098660, PubMed:1339418, PubMed:4560498, PubMed:7016177). The enzyme is stereoselective for the S-enantiomer of KHG (PubMed:1098660, PubMed:4560498). Cleavage of KHG could serve in tricarboxylic acid (TCA) cycle regulation or, when operating in the reverse direction, in the detoxification of glyoxylate (Probable). Finally, also shows a high level of oxaloacetate beta-decarboxylase activity (PubMed:1339418, PubMed:4560498)...

## Biological Role

Repressed by cra (protein.P0ACP1), gntR (protein.P0ACP5), phoB (protein.P0AFJ5), plaR (protein.P37671), kdgR (protein.P76268). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A955|protein.P0A955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=eda; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=eda; function=-
- `represses` <-- [[protein.P0ACP5|protein.P0ACP5]] `RegulonDB` `S` - regulator=GntR; target=eda; function=-
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=eda; function=-
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=eda; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76268|protein.P76268]] `RegulonDB` `S` - regulator=KdgR; target=eda; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006164,ECOCYC:EG10256,GeneID:946367`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1932115-1932756:-; feature_type=gene
