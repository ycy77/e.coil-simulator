---
entity_id: "gene.b3831"
entity_type: "gene"
name: "udp"
source_database: "NCBI RefSeq"
source_id: "gene-b3831"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3831"
  - "udp"
---

# udp

`gene.b3831`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3831`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

udp (gene.b3831) is a gene entity. It encodes udp (protein.P12758). Encoded protein function: FUNCTION: Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and ribose-1-phosphate (PubMed:16751). Shows weak activity towards deoxyuridine and thymidine (PubMed:16751). The produced molecules are then utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis (Probable). {ECO:0000269|PubMed:16751, ECO:0000305}. EcoCyc product frame: URPHOS-MONOMER. Genomic coordinates: 4016431-4017192. EcoCyc protein note: Uridine phosphorylase (Udp) catalyzes the reversible phosphorolysis of uridine with the formation of ribose-1-phosphate and uracil . Udp belongs to the UP-1 subfamily of the nucleoside phosphorylase superfamily 1 . Udp is involved in utilization of nucleosides as a carbon and energy source and is part of a process that degrades "overflow" UMP nucleotides . The main activity of Udp is towards uracil ribonucleotides, but some activity is retained towards deoxyuridine and thymidine . The substrate specificity of the enzyme has been evaluated using a large set of modified nucleosides . The catalytic mechanism has been investigated . The Asp5 carboxyl group is important for catalysis . Various crystal structures of the enzyme alone or bound to substrates or inhibitors have been determined...

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12758|protein.P12758]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=udp; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=udp; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=udp; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=udp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012528,ECOCYC:EG11045,GeneID:948987`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4016431-4017192:+; feature_type=gene
