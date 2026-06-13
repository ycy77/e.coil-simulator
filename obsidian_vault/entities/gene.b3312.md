---
entity_id: "gene.b3312"
entity_type: "gene"
name: "rpmC"
source_database: "NCBI RefSeq"
source_id: "gene-b3312"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3312"
  - "rpmC"
---

# rpmC

`gene.b3312`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3312`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmC (gene.b3312) is a gene entity. It encodes rpmC (protein.P0A7M6). Encoded protein function: FUNCTION: Binds 23S rRNA. It is not essential for growth. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:6170935}.; FUNCTION: One of the proteins that surrounds the polypeptide exit tunnel on the outside of the subunit. Contacts trigger factor (PubMed:12226666). {ECO:0000269|PubMed:12226666}. EcoCyc product frame: EG10887-MONOMER. Genomic coordinates: 3448568-3448759. EcoCyc protein note: The L29 protein is a component of the 50S subunit of the ribosome . L29 interacts with 23S rRNA and is photoaffinity labeled by puromycin, an analog of the 3' end of aminoacylated tRNA . L29 crosslinks to Trigger Factor (TF) and contacts the Signal Recognition Particle , but is not required for the association of TF with the ribosome . L29 together with ACP stimulates the binding of Tn7-encoded TnsD to attTn7, the insertion site for Tn7 in the E. coli chromosome. L23 also stimulates Tn7 transposition in vitro. A mutation in L29 decreases Tn7 transposition in vivo .

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7M6|protein.P0A7M6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpmC; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rpmC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010842,ECOCYC:EG10887,GeneID:947807`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3448568-3448759:-; feature_type=gene
