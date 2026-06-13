---
entity_id: "gene.b2341"
entity_type: "gene"
name: "fadJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2341"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2341"
  - "fadJ"
---

# fadJ

`gene.b2341`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2341`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadJ (gene.b2341) is a gene entity. It encodes fadJ (protein.P77399). Encoded protein function: FUNCTION: Catalyzes the formation of a hydroxyacyl-CoA by addition of water on enoyl-CoA. Also exhibits 3-hydroxyacyl-CoA epimerase and 3-hydroxyacyl-CoA dehydrogenase activities. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}. EcoCyc product frame: G7212-MONOMER. EcoCyc synonyms: yfcX. Genomic coordinates: 2457015-2459159. EcoCyc protein note: During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway . FadJ shows sequence similarity to FadB; the enoyl-CoA hydratase, 3-hydroxyacyl-CoA epimerase, and 3-hydroxyacyl-CoA dehydrogenase active site residues appear to be conserved. In a strain engineered for polyhydroxyalkanoate (PHA) production, FadJ is essential for processing of long-chain fatty acids to medium-chain PHA if fadB is absent. Crude cell extracts from a strain that overproduced FadJ contain increased enoyl-CoA hydratase and 3-hydroxyacyl-CoA dehydrogenase activity...

## Biological Role

Repressed by fadR (protein.P0A8V6), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77399|protein.P77399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fadJ; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=fadJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007723,ECOCYC:G7212,GeneID:949097`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2457015-2459159:-; feature_type=gene
