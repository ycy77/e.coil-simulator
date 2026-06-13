---
entity_id: "gene.b2582"
entity_type: "gene"
name: "trxC"
source_database: "NCBI RefSeq"
source_id: "gene-b2582"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2582"
  - "trxC"
---

# trxC

`gene.b2582`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2582`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trxC (gene.b2582) is a gene entity. It encodes trxC (protein.P0AGG4). Encoded protein function: FUNCTION: Efficient electron donor for the essential enzyme ribonucleotide reductase. Is also able to reduce the interchain disulfide bridges of insulin. EcoCyc product frame: OX-THIOREDOXIN2-MONOMER. EcoCyc synonyms: yfiG. Genomic coordinates: 2718735-2719154. EcoCyc protein note: Thioredoxins are small electron transfer proteins that contain a cysteine disulfide/dithiol active site with the amino acid sequence motif Cys-X-X-Cys (where X is any amino acid). They are members of the thioredoxin protein family. Members of this family/superfamily contain the thioredoxin fold, a characteristic and stable protein fold consisting of four β-sheets surrounded by three α-helices (reviewed in ). The proteins function in a wide variety of cellular processes. Thioredoxin is reduced by NADPH in a reaction catalyzed by thioredoxin reductase. The conversion between the oxidized and reduced forms results in a subtle change of conformation. The functional properties differ between the two forms of thioredoxin. The reduced form of thioredoxin is a protein disulfide reductase, and catalyzes dithiol-disulfide exchange reactions. Escherichia coli thioredoxin contains the active site amino acid sequence Trp-Cys-Gly-Pro-Cys. In and reviewed in...

## Biological Role

Activated by oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGG4|protein.P0AGG4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=trxC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008501,ECOCYC:EG11887,GeneID:947062`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2718735-2719154:+; feature_type=gene
