---
entity_id: "gene.b0783"
entity_type: "gene"
name: "moaC"
source_database: "NCBI RefSeq"
source_id: "gene-b0783"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0783"
  - "moaC"
---

# moaC

`gene.b0783`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0783`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moaC (gene.b0783) is a gene entity. It encodes moaC (protein.P0A738). Encoded protein function: FUNCTION: Catalyzes the conversion of (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate to cyclic pyranopterin monophosphate (cPMP). {ECO:0000255|HAMAP-Rule:MF_01224, ECO:0000269|PubMed:25941396}. EcoCyc product frame: EG11666-MONOMER. EcoCyc synonyms: chlA3. Genomic coordinates: 818570-819055.

## Biological Role

Activated by fnr (protein.P0A9E5), modE (protein.P0A9G8), csrA (protein.P69913).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A738|protein.P0A738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moaC; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=moaC; function=+
- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=CsrA; target=moaC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002673,ECOCYC:EG11666,GeneID:945397`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:818570-819055:+; feature_type=gene
