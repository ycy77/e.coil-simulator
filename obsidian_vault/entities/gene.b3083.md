---
entity_id: "gene.b3083"
entity_type: "gene"
name: "higB"
source_database: "NCBI RefSeq"
source_id: "gene-b3083"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3083"
  - "higB"
---

# higB

`gene.b3083`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3083`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

higB (gene.b3083) is a gene entity. It encodes higB (protein.P64578). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-dependent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome by subsequent expression of antitoxin HigA. Overexpression causes cleavage of a number of mRNAs in a translation-dependent fashion, suggesting this is an mRNA interferase. {ECO:0000269|PubMed:19943910}. EcoCyc product frame: G7602-MONOMER. EcoCyc synonyms: ygjN. Genomic coordinates: 3234141-3234455. EcoCyc protein note: HigB is the toxin of the HigB-HigA toxin-antitoxin system, acting as a translation-dependent mRNA interferase. HigB inhibits protein synthesis by cleaving translated mRNAs within the coding region . It also is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . An analysis of the targets and site specificity showed that HigB favors a G nucleotide downstream of the cleavage site and shows strong codon position preference. Like other E. coli endoribonuclease toxins, HigB activity does not affect mature ribosomes, but inhibits ribosome biogenesis, likely by affecting the translation of a specific set of ribosomal proteins...

## Biological Role

Repressed by higA (protein.P67701). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64578|protein.P64578]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=higB; function=+
- `represses` <-- [[protein.P67701|protein.P67701]] `RegulonDB` `S` - regulator=HigA; target=higB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010128,ECOCYC:G7602,GeneID:947591`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3234141-3234455:-; feature_type=gene
