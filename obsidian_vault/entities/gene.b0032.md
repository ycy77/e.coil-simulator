---
entity_id: "gene.b0032"
entity_type: "gene"
name: "carA"
source_database: "NCBI RefSeq"
source_id: "gene-b0032"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0032"
  - "carA"
---

# carA

`gene.b0032`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0032`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

carA (gene.b0032) is a gene entity. It encodes carA (protein.P0A6F1). Encoded protein function: FUNCTION: Small subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The small subunit (glutamine amidotransferase) binds and cleaves glutamine to supply the large subunit with the substrate ammonia. {ECO:0000255|HAMAP-Rule:MF_01209, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.10}. EcoCyc product frame: CARBPSYN-SMALL. EcoCyc synonyms: arg, pyrA. Genomic coordinates: 29651-30799. EcoCyc protein note: The small subunit encoded by carA is the amidotransferase component of the enzyme. It hydrolyzes glutamine to glutamate and ammonia. The small subunit contains a catalytic triad (Cys269, His353 and Glu355) situated between the two structural domains . The small subunit is protected from proteolysis by the large subunit . The mechanism for glutamine hydrolysis on the small subunit requires the participation of an essential sulfhydryl group for the formation of a thioester intermediate...

## Biological Role

Repressed by argR (protein.P0A6D0), purR (protein.P0ACP7), pepA (protein.P68767). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), rutR (protein.P0ACU2).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6F1|protein.P0A6F1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=carA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=carA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=carA; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=carA; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=carA; function=-
- `represses` <-- [[protein.P68767|protein.P68767]] `RegulonDB` `S` - regulator=PepA; target=carA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000118,ECOCYC:EG10134,GeneID:949025`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:29651-30799:+; feature_type=gene
