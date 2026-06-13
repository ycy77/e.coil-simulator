---
entity_id: "gene.b1203"
entity_type: "gene"
name: "ychF"
source_database: "NCBI RefSeq"
source_id: "gene-b1203"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1203"
  - "ychF"
---

# ychF

`gene.b1203`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1203`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychF (gene.b1203) is a gene entity. It encodes ychF (protein.P0ABU2). Encoded protein function: FUNCTION: ATPase that binds to both the 70S ribosome and the 50S ribosomal subunit in a nucleotide-independent manner. Does not hydrolyze GTP. {ECO:0000255|HAMAP-Rule:MF_00944, ECO:0000269|PubMed:21527254}. EcoCyc product frame: EG11404-MONOMER. EcoCyc synonyms: gtp1. Genomic coordinates: 1256721-1257812. EcoCyc protein note: The highly conserved YchF protein is a HAS-ATPase, the founding member of a family of GTP-binding proteins with ATPase activity . The conservation and essentiality of this protein in many bacteria points to an ancient origin associated with cell survival in a variety of environments . The bacterial GTPase superfamily is associated with RNA- and translation-related roles in the cell . The ATPase activity of YchF appears to be redox-regulated . YchF regulates adaptation of the cell to various stress conditions by interacting with EG10506-MONOMER, inhibiting leaderless mRNA translation and its association with the CPLX0-3953 . Additionally it inhibits production of the major stress response RPOS-MONOMER as well as polyphosphate levels via regulation of PPK-MONOMER . YchF has K+-activated ATPase activity and binds to both the 70S ribosome and the 50S ribosomal subunit in a nucleotide-independent manner...

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABU2|protein.P0ABU2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ychF; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=ychF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004038,ECOCYC:EG11404,GeneID:945769`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1256721-1257812:-; feature_type=gene
