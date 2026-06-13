---
entity_id: "gene.b4147"
entity_type: "gene"
name: "efp"
source_database: "NCBI RefSeq"
source_id: "gene-b4147"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4147"
  - "efp"
---

# efp

`gene.b4147`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4147`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

efp (gene.b4147) is a gene entity. It encodes efp (protein.P0A6N4). Encoded protein function: FUNCTION: Involved in peptide bond synthesis. Alleviates ribosome stalling that occurs when 3 or more consecutive proline residues or the sequence Pro-Pro-Gly is present in a protein, by stabilizing the P-site tRNA thus promoting a favorable geometry for peptide bond formation (PubMed:23239623, PubMed:23239624, PubMed:29100052). Alleviates ribosome stalling at di-Pro-containing sequences; in rare cases motifs lacking di-Pro can also be targeted (PubMed:39622818). Beta-lysylation at Lys-34 is required for alleviation. The Pro codons and their context do not affect activity; only consecutive Pro residues (not another amino acid) are affected by EF-P. Has stimulatory effects on peptide bond formation between ribosome-bound initiator tRNA(fMet) and puromycin, and N-acetyl-Phe tRNA(Phe)-primed poly(U)-directed poly(Phe) synthesis. Its function partially overlaps with EfpL and UUP (PubMed:39622818). A tRNA(Pro) in the P-site and guanosine in the first position of the E-site codon promote EF-P (and EfpL) binding to the ribosome (Probable) (PubMed:39622818). Can also cause translational pausing, probably by blocking tRNA translocation to the E-site (PubMed:39622818). {ECO:0000269|PubMed:23239623, ECO:0000269|PubMed:23239624, ECO:0000269|PubMed:39622818}. EcoCyc product frame: MONOMER0-4200...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6N4|protein.P0A6N4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013583,ECOCYC:EG12099,GeneID:948661`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4375699-4376265:+; feature_type=gene
