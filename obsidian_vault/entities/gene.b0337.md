---
entity_id: "gene.b0337"
entity_type: "gene"
name: "codA"
source_database: "NCBI RefSeq"
source_id: "gene-b0337"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0337"
  - "codA"
---

# codA

`gene.b0337`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0337`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

codA (gene.b0337) is a gene entity. It encodes codA (protein.P25524). Encoded protein function: FUNCTION: Catalyzes the hydrolytic deamination of cytosine to uracil. Is involved in the pyrimidine salvage pathway, which allows the cell to utilize cytosine for pyrimidine nucleotide synthesis. Is also able to catalyze deamination of isoguanine, a mutagenic oxidation product of adenine in DNA, and of isocytosine. To a lesser extent, also catalyzes the conversion of 5-fluorocytosine (5FC) to 5-fluorouracil (5FU); this activity allows the formation of a cytotoxic chemotherapeutic agent from a non-cytotoxic precursor. {ECO:0000269|PubMed:15381761, ECO:0000269|PubMed:21545144, ECO:0000269|PubMed:21604715, ECO:0000269|PubMed:8226944}. EcoCyc product frame: CYTDEAM-MONOMER. Genomic coordinates: 356171-357454.

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25524|protein.P25524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=codA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `C` - regulator=Nac; target=codA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001161,ECOCYC:EG11326,GeneID:944996`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:356171-357454:+; feature_type=gene
