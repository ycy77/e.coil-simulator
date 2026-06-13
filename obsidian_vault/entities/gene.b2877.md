---
entity_id: "gene.b2877"
entity_type: "gene"
name: "mocA"
source_database: "NCBI RefSeq"
source_id: "gene-b2877"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2877"
  - "mocA"
---

# mocA

`gene.b2877`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2877`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mocA (gene.b2877) is a gene entity. It encodes mocA (protein.Q46810). Encoded protein function: FUNCTION: Transfers a CMP moiety from CTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin cytosine dinucleotide (Mo-MCD) cofactor. Is specific for CTP; other nucleotides such as ATP and GTP cannot be utilized. Is also able to convert MPT to MCD in the absence of molybdate, however, with only one catalytic turnover. {ECO:0000269|PubMed:19542235}. EcoCyc product frame: G7496-MONOMER. EcoCyc synonyms: ygfJ. Genomic coordinates: 3015160-3015738. EcoCyc protein note: MocA is a molybdenum cofactor cytidylyltransferase belonging to the NTP transferase superfamily of proteins. The enzyme catalyzes the transfer of a CMP moiety from CTP to Mo-molybdopterin, forming MCD . The specificity of MocA for CTP was also investigated, showing that the N-terminal domain determines nucleotide recognition and binding. The C-terminal domain is responsible for interacting with the specific acceptor protein G6154-MONOMER PaoD . A mocA mutant contains inactive CPLX0-7805 lacking molybdenum and is thus unable to grow on medium containing cinnamaldehyde . Reviews:

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46810|protein.Q46810]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009447,ECOCYC:G7496,GeneID:947356`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3015160-3015738:+; feature_type=gene
