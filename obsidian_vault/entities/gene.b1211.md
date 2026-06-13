---
entity_id: "gene.b1211"
entity_type: "gene"
name: "prfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1211"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1211"
  - "prfA"
---

# prfA

`gene.b1211`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1211`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prfA (gene.b1211) is a gene entity. It encodes prfA (protein.P0A7I0). Encoded protein function: FUNCTION: Peptide chain release factor 1 directs the termination of translation in response to the peptide chain termination codons UAG and UAA. EcoCyc product frame: EG10761-MONOMER. EcoCyc synonyms: ups?, sueB, uar. Genomic coordinates: 1265012-1266094. EcoCyc protein note: Release factor 1 (RF1) is one of two class 1 codon-specific factors in E. coli that facilitate the release of the growing polypeptide chain at stop codons. RF1 recognizes the termination codons UAG and UAA ; EG10762-MONOMER RF2 recognizes UGA and UAA. In E. coli, the UAG stop codon is relatively rare, terminating only ~7% of all protein-coding genes including only seven essential genes . Termination is highly precise; RF1 is able to discriminate against related sense codons by 3 to 6 orders of magnitude and without requiring energy-driven error correction . The discriminator site consists of a tripeptide which appears to be functionally equivalent to the anticodon of tRNA . The I196 and L126 amino acids contribute to discrimination between the different stop codons . An E. coli cell is variously estimated to contain between 500 and 4900 molecules of RF1 and reaches the highest RF1 content at a high growth rate . RF1 is less abundant than RF2 under most growth conditions...

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7I0|protein.P0A7I0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=prfA; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=prfA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004066,ECOCYC:EG10761,GeneID:949002`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1265012-1266094:+; feature_type=gene
