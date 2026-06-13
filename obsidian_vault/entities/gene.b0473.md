---
entity_id: "gene.b0473"
entity_type: "gene"
name: "htpG"
source_database: "NCBI RefSeq"
source_id: "gene-b0473"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0473"
  - "htpG"
---

# htpG

`gene.b0473`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0473`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

htpG (gene.b0473) is a gene entity. It encodes htpG (protein.P0A6Z3). Encoded protein function: FUNCTION: Molecular chaperone. Has ATPase activity. EcoCyc product frame: EG10461-MONOMER. Genomic coordinates: 495120-496994. EcoCyc protein note: HtpG is a member of the Hsp90 (heat shock protein, 90kDa) family of molecular chaperones . Purified HtpG is an ATPase (with a kcat of 0.011 sec-1 and a KM for ATP of 250 µM ). Purified, immobilised HtpG binds the heat shock alternative sigma factor σ32 and an unidentified cyclophilin (peptidyl-prolyl isomerase) . HtpG participates in the folding of newly synthesized proteins under mild heat shock conditions ; purified HtpG suppresses the thermal aggregation of citrate synthase at 43°C (see also ). HtpG collaborates with the EG10241-MONOMER "DnaK" chaperone system to reactivate inactive protein substrates; the ATPase activity of HtpG is essential for this activity; HtpG and DnaK physically interact in vivo and in vitro (see further ). HtpG binds partially folded states of a model substrate (Staphylococcal nuclease) that are transiently sampled from its thermodynamically stable native state . HtpG is a phosphoprotein in vivo ; the purified protein acquires 1.5 phosphate groups/molecule predominantly on serine and threonine residues but also on a His residue...

## Biological Role

Repressed by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), ascG (protein.P24242), nac (protein.Q47005). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Z3|protein.P0A6Z3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=htpG; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P24242|protein.P24242]] `RegulonDB` `S` - regulator=AscG; target=htpG; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=htpG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001642,ECOCYC:EG10461,GeneID:945099`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:495120-496994:+; feature_type=gene
