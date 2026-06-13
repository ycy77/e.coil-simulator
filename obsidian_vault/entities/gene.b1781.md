---
entity_id: "gene.b1781"
entity_type: "gene"
name: "yeaE"
source_database: "NCBI RefSeq"
source_id: "gene-b1781"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1781"
  - "yeaE"
---

# yeaE

`gene.b1781`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1781`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaE (gene.b1781) is a gene entity. It encodes yeaE (protein.P76234). Encoded protein function: FUNCTION: Aldo-keto reductase that contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Can also use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}. EcoCyc product frame: G6967-MONOMER. Genomic coordinates: 1864782-1865636. EcoCyc protein note: YeaE has been shown to have methylglyoxal reductase activity . The subunit structure of YeaE has not been determined, but its amino acid sequence similarity to the aldo-keto reductases DkgA (YqhE) and DkgB (YafB) suggests that it may be monomeric . Growth of a yeaE gloA double mutant is inhibited by 0.3 mM methylglyoxal . A yeaE mutant is more sensitive to glyoxal than wild type in plate assays, although the IC50 in a liquid assay is quite similar to that of wild type . Expression of yeaE is not increased in response to methylglyoxal or glyoxal . Review:

## Biological Role

Repressed by DNA-binding transcriptional dual regulator NsrR (complex.ecocyc.CPLX0-7756), NtrC phosphorylated dimer (complex.ecocyc.CPLX0-8566), lrp (protein.P0ACJ0), glnG (protein.P0AFB8), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76234|protein.P76234]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `represses` <-- [[complex.ecocyc.CPLX0-7756|complex.ecocyc.CPLX0-7756]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=yeaE; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yeaE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005925,ECOCYC:G6967,GeneID:946302`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1864782-1865636:-; feature_type=gene
