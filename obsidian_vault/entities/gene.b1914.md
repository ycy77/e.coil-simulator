---
entity_id: "gene.b1914"
entity_type: "gene"
name: "uvrY"
source_database: "NCBI RefSeq"
source_id: "gene-b1914"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1914"
  - "uvrY"
---

# uvrY

`gene.b1914`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1914`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uvrY (gene.b1914) is a gene entity. It encodes uvrY (protein.P0AED5). Encoded protein function: FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). UvrY activates the transcription of the untranslated csrB RNA and of barA, in an autoregulatory loop. Mediates the effects of CsrA on csrB RNA by BarA-dependent and BarA-independent mechanisms (PubMed:12193630). {ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}. EcoCyc product frame: MONOMER0-1. EcoCyc synonyms: yecB. Genomic coordinates: 1994703-1995359. EcoCyc protein note: UvrY, which belongs to the LuxR/UhpA family, is the transcriptional regulator of the EG11367 BarA/EG11140 UvrY two-component signal transduction system which plays a role in central carbon metabolism via its regulation of the small non-coding RNAs CSRC-RNA "CsrC and CSRB-RNA "CsrB". BarA senses and responds to the presence of the protonated form of short-chain carboxylic acids such as FORMATE "formic acid" and ACET "acetic acid", which accumulate at the late exponential phase of growth on acetogenic substrates such as glucose. Upon sensing of these products, BarA autophosphorylates, followed by transphosphorylation of UvrY at the conserved Asp54 residue...

## Biological Role

Repressed by nac (protein.Q47005). Activated by ATP-dependent RNA helicase DeaD (complex.ecocyc.CPLX0-8557), rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AED5|protein.P0AED5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-8557|complex.ecocyc.CPLX0-8557]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uvrY; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=uvrY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006373,ECOCYC:EG11140,GeneID:946424`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1994703-1995359:-; feature_type=gene
