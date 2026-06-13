---
entity_id: "gene.b2010"
entity_type: "gene"
name: "dacD"
source_database: "NCBI RefSeq"
source_id: "gene-b2010"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2010"
  - "dacD"
---

# dacD

`gene.b2010`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2010`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dacD (gene.b2010) is a gene entity. It encodes dacD (protein.P33013). Encoded protein function: FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors. EcoCyc product frame: RPOA-MONOMER. EcoCyc synonyms: phsE, yeeC. Genomic coordinates: 2081381-2082547. EcoCyc protein note: Penicillin-binding protein 6b (PBP6b), the product of the dacD gene, is a penicillin-sensitive, membrane-bound D-alanyl D-alanine carboxypeptidase (DD-carboxypeptidase) which cleaves the carboxy-terminal D-alanine from peptidoglycan pentapeptides . PBP6b DD-carboxypeptidase activity contributes to the maintenance of cell shape at low pH . The predicted amino acid sequence of PBP6b is 47.4% identical to CPLX0-8252 "PBP5" and 47.7% identical to CPLX0-8254 "PBP6" . Increased expression of dacD in a strain that contains dacA and dacC null alleles reduces the amount of pentapeptide muropeptides in peptidoglycan . DacD contains the conserved motif sequences, SxxK (SLTK), [S/Y]xN (SGN) and [K/H][T/S]G (KTG), of the serine acyltransferase superfamily ; DacD binds benzylpenicillin . DacD does not contribute to intrinsic β-lactam resistance in E. coli K-12, however overexpression of dacD partially complements the β-lactam sensitivity of a ΔdacA mutant...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33013|protein.P33013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006680,ECOCYC:EG11893,GeneID:946518`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2081381-2082547:-; feature_type=gene
