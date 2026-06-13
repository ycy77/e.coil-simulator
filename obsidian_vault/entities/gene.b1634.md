---
entity_id: "gene.b1634"
entity_type: "gene"
name: "dtpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1634"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1634"
  - "dtpA"
---

# dtpA

`gene.b1634`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1634`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dtpA (gene.b1634) is a gene entity. It encodes dtpA (protein.P77304). Encoded protein function: FUNCTION: Proton-dependent permease that transports di- and tripeptides as well as structurally related peptidomimetics such as aminocephalosporins into the cell. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:15175316, ECO:0000269|PubMed:17158458, ECO:0000269|PubMed:18485005}. EcoCyc product frame: B1634-MONOMER. EcoCyc synonyms: ydgR, tppB. Genomic coordinates: 1712769-1714271. EcoCyc protein note: The DtpA protein (formerly TppB) is a member of the POT (proton-dependent oligopeptide transporter) family of peptide transporters also known as the PTR (peptide transport) family. DtpA is responsible for proton-dependent transport of di- and tripeptides as well as some structurally related peptidomimetics like B-lactam antibiotics . DtpA transports the tetrapeptide, tetraalanine in vitro however tetraalanine does not function as an inhibitor in competitive transport assays . DtpA shows a preference for di- and tripeptides composed of L amino acids and for peptides containing a positively charged side chain in the N-terminal position...

## Biological Role

Repressed by lrp (protein.P0ACJ0), gadX (protein.P37639). Activated by rpoD (protein.P00579), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77304|protein.P77304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dtpA; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=dtpA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=dtpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=dtpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005469,ECOCYC:G6877,GeneID:947436`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1712769-1714271:+; feature_type=gene
