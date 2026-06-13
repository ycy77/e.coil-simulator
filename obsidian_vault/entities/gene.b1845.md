---
entity_id: "gene.b1845"
entity_type: "gene"
name: "ptrB"
source_database: "NCBI RefSeq"
source_id: "gene-b1845"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1845"
  - "ptrB"
---

# ptrB

`gene.b1845`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1845`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptrB (gene.b1845) is a gene entity. It encodes ptrB (protein.P24555). Encoded protein function: FUNCTION: Cleaves peptide bonds on the C-terminal side of lysyl and argininyl residues. EcoCyc product frame: EG11004-MONOMER. EcoCyc synonyms: tlp. Genomic coordinates: 1926779-1928839. EcoCyc protein note: Oligopeptidase B, originally called protease II, is a serine protease that hydrolyzes peptide bonds following arginines and lysines . The enzyme is very efficient at cleaving after paired basic amino acid residues such as Arg-Arg . Its specificity for artificial peptide substrates has been compared with EG11441-MONOMER and oligopeptidases from other organisms . PtrB is able to degrade and thereby inactivate several short antimicrobial peptides (AMPs) . The enzyme belongs to the prolyl oligopeptidase family of serine peptidases . A noncanonical translation initiation mechanism was discovered for PtrB. The ptrB mRNA begins with an AUG codon at its very 5' end (5'-uAUG). Although translation of the potential 5' ORF is poor, the 5'-uAUG is required for efficent translation of PtrB . The 5'-uAUG functions as a ribosome recognition signal that compensates for the poor Shine-Dalgarno sequence upstream of the ptrB ORF . Overexpression of ptrB from a plasmid confers increased resistance to the proline-rich antimicrobial peptide Bac7(1-16) and certain other AMPs...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24555|protein.P24555]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006133,ECOCYC:EG11004,GeneID:946358`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1926779-1928839:-; feature_type=gene
