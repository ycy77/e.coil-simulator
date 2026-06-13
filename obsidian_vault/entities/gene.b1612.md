---
entity_id: "gene.b1612"
entity_type: "gene"
name: "fumA"
source_database: "NCBI RefSeq"
source_id: "gene-b1612"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1612"
  - "fumA"
---

# fumA

`gene.b1612`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1612`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fumA (gene.b1612) is a gene entity. It encodes fumA (protein.P0AC33). Encoded protein function: FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions as an aerobic enzyme in the direction of malate formation as part of the citric acid cycle. Accounts for about 80% of the fumarase activity when the bacteria grow aerobically. To a lesser extent, also displays D-tartrate dehydratase activity in vitro, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Can also catalyze the isomerization of enol- to keto-oxaloacetate. {ECO:0000269|PubMed:1329945, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:8422384, ECO:0000269|Ref.7}. EcoCyc product frame: FUMA-MONOMER. Genomic coordinates: 1686731-1688377. EcoCyc protein note: Fumarase A (FumA) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumA is a dimeric [4Fe-4S] cluster-containing protein and belongs to the class I fumarases . Fumarase A can also catalyze the isomerization of enol- to keto-oxalacetate . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC33|protein.P0AC33]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fumA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=fumA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005392,ECOCYC:EG10356,GeneID:946826`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1686731-1688377:-; feature_type=gene
