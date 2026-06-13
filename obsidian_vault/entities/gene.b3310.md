---
entity_id: "gene.b3310"
entity_type: "gene"
name: "rplN"
source_database: "NCBI RefSeq"
source_id: "gene-b3310"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3310"
  - "rplN"
---

# rplN

`gene.b3310`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3310`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplN (gene.b3310) is a gene entity. It encodes rplN (protein.P0ADY3). Encoded protein function: FUNCTION: Binds to 23S rRNA. Forms part of two intersubunit bridges in the 70S ribosome. {ECO:0000255|HAMAP-Rule:MF_01367}.; FUNCTION: In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA in bridges B5 and B8 (PubMed:12809609, PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}.; FUNCTION: Can interact with RsfS, in this case bridge B8 probably cannot form, and the 30S and 50S ribosomal subunits do not associate, which represses translation (PubMed:22829778, PubMed:33639093). {ECO:0000269|PubMed:22829778, ECO:0000269|PubMed:33639093}. EcoCyc product frame: EG10875-MONOMER. Genomic coordinates: 3447778-3448149. EcoCyc protein note: The L14 protein is a component of the 50S subunit of the ribosome. L14 crosslinks to 23S rRNA . In the cryo-EM reconstruction of the ribosome, L14 was modelled to be located at the 30S-50S subunit interface, at bridges B5 and B8 . In all-atom molecular dynamics simulations of the ribosome, a structural gate between helices 71 and 92 of 23S rRNA restricts tRNA motion and together with L14 acts as a steric filter for the cognate tRNA . L14 interacts directly with EG11255-MONOMER. Amino acid residues in L14 that are essential for this interaction have been identified by mutagenesis...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADY3|protein.P0ADY3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010837,ECOCYC:EG10875,GeneID:947809`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3447778-3448149:-; feature_type=gene
