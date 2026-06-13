---
entity_id: "gene.b1534"
entity_type: "gene"
name: "ydeE"
source_database: "NCBI RefSeq"
source_id: "gene-b1534"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1534"
  - "ydeE"
---

# ydeE

`gene.b1534`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1534`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeE (gene.b1534) is a gene entity. It encodes ydeE (protein.P31126). Encoded protein function: FUNCTION: A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:20067529}. EcoCyc product frame: YDEF-MONOMER. EcoCyc synonyms: ydeF. Genomic coordinates: 1621332-1622519. EcoCyc protein note: YdeE is a member of the Drug:H+ Antiporter-1 (DHA) family within the Major Facilitator Superfamily (MFS) of transporters . YdeE has been implicated in arabinose efflux . YdeE is able to transport dipeptides (Ala-Gln and L-alanyl-L-branched chain amino acids) in a dipeptide overproducing strain . Overexpression of cloned ydeE (ydeF) in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of antibiotics, dyes and toxic compounds...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), gcvB (gene.b4443), lrp (protein.P0ACJ0). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31126|protein.P31126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydeE; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=ydeE; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005121,ECOCYC:EG11640,GeneID:946083`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1621332-1622519:+; feature_type=gene
