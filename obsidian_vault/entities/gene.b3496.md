---
entity_id: "gene.b3496"
entity_type: "gene"
name: "dtpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3496"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3496"
  - "dtpB"
---

# dtpB

`gene.b3496`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3496`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dtpB (gene.b3496) is a gene entity. It encodes dtpB (protein.P36837). Encoded protein function: FUNCTION: Proton-dependent permease that transports di- and tripeptides. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:18485005}. EcoCyc product frame: YHIP-MONOMER. EcoCyc synonyms: yhiP. Genomic coordinates: 3640862-3642331. EcoCyc protein note: The DtpB protein is a member of the POT (proton-dependent oligopeptide transporter) family of peptide transporters . DtpB is responsible for proton-dependent transport of di- and tripeptides as well as some structurally related peptidomimetics like B-lactam antibiotics . DtpB transports the tetrapeptide, tetraalanine in vitro however tetraalanine does not function as an inhibitor in competitive transport assays . DtpB shows a preference for di- and tripeptides composed of L amino acids and for peptides containing a positively charged side chain in the N-terminal position . YhiP is predicted to contain 14 transmembrane regions with the C-terminus located in the cytoplasm . The dipeptide/tripeptide:proton symporters DtpB and B1634-MONOMER DtpA are receptors for the group 6 contact-dependent growth inhibition (CDI) ionophore toxins . dtpB: dipeptide and tripeptide permease B

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36837|protein.P36837]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011417,ECOCYC:EG12232,GeneID:948006`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3640862-3642331:+; feature_type=gene
