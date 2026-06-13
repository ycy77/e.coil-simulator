---
entity_id: "gene.b0595"
entity_type: "gene"
name: "entB"
source_database: "NCBI RefSeq"
source_id: "gene-b0595"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0595"
  - "entB"
---

# entB

`gene.b0595`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0595`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entB (gene.b0595) is a gene entity. It encodes entB (protein.P0ADI4). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(3+) atoms. EntB is a bifunctional protein that serves as an isochorismate lyase and an aryl carrier protein (ArCP). Catalyzes the conversion of isochorismate to 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), the precursor of 2,3-dihydroxybenzoate (DHB). In the enterobactin assembly, EntB functions as an aryl carrier protein phosphopantetheinylated near the C terminus by EntD to yield holo-EntB, which is then acylated by EntE with 2,3-dihydroxybenzoyl-AMP to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. {ECO:0000269|PubMed:16567620, ECO:0000269|PubMed:16632253, ECO:0000269|PubMed:19699210, ECO:0000269|PubMed:2139796, ECO:0000269|PubMed:2172214, ECO:0000269|PubMed:2531000, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}. EcoCyc product frame: HOLO-ENTB. EcoCyc synonyms: entG. Genomic coordinates: 627694-628551...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADI4|protein.P0ADI4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=entB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002052,ECOCYC:EG10260,GeneID:946178`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:627694-628551:+; feature_type=gene
