---
entity_id: "protein.P30015"
entity_type: "protein"
name: "lhr"
source_database: "UniProt"
source_id: "P30015"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lhr rhlF b1653 JW1645"
---

# lhr

`protein.P30015`

## Static

- Type: `protein`
- Source: `UniProt:P30015`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A 3'-5' helicase probably involved in DNA repair. Translocates in an ATP-dependent manner 3'-to-5' on single-stranded (ss)DNA, unwinding any encountered duplex nucleic acid (PubMed:33744958). An RNA:DNA hybrid with a 3'-ssDNA loading strand is a 4.5-fold better helicase substrate than 3'-tailed double-stranded (ds)DNA; substrates where the helicase loads on a 3'-ssRNA tail (DNA:RNA and RNA:RNA) are not unwound (PubMed:33744958). Unlike its M.smegmatis counterpart, the ATPase is not ssDNA-dependent (PubMed:33744958). Forms a clamp around the ssDNA loading strand (By similarity). {ECO:0000250|UniProtKB:A0QT91, ECO:0000269|PubMed:33744958}.; FUNCTION: Excises uracil residues from DNA; forked DNA with a dU residue is the best substrate followed by ssDNA (PubMed:37452011). Inactive on dsDNA with a dU residue or DNA with an 8-oxoguanine residue (PubMed:37452011). Uracil residues in DNA can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine. {ECO:0000269|PubMed:37452011}.

## Biological Role

Component of ATP-dependent helicase/uracil glycosylase Lhr (complex.ecocyc.CPLX0-8581).

## Annotation

FUNCTION: A 3'-5' helicase probably involved in DNA repair. Translocates in an ATP-dependent manner 3'-to-5' on single-stranded (ss)DNA, unwinding any encountered duplex nucleic acid (PubMed:33744958). An RNA:DNA hybrid with a 3'-ssDNA loading strand is a 4.5-fold better helicase substrate than 3'-tailed double-stranded (ds)DNA; substrates where the helicase loads on a 3'-ssRNA tail (DNA:RNA and RNA:RNA) are not unwound (PubMed:33744958). Unlike its M.smegmatis counterpart, the ATPase is not ssDNA-dependent (PubMed:33744958). Forms a clamp around the ssDNA loading strand (By similarity). {ECO:0000250|UniProtKB:A0QT91, ECO:0000269|PubMed:33744958}.; FUNCTION: Excises uracil residues from DNA; forked DNA with a dU residue is the best substrate followed by ssDNA (PubMed:37452011). Inactive on dsDNA with a dU residue or DNA with an 8-oxoguanine residue (PubMed:37452011). Uracil residues in DNA can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine. {ECO:0000269|PubMed:37452011}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8581|complex.ecocyc.CPLX0-8581]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1653|gene.b1653]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30015`
- `KEGG:ecj:JW1645;eco:b1653;ecoc:C3026_09485;`
- `GeneID:946156;`
- `GO:GO:0003677; GO:0004844; GO:0005524; GO:0006284; GO:0006979; GO:0016887; GO:0033679; GO:0042802; GO:0043138; GO:0097510`
- `EC:3.2.2.27; 5.6.2.-; 5.6.2.4`

## Notes

Lhr helicase/uracil glycosylase (EC 3.2.2.27) (EC 5.6.2.-) (EC 5.6.2.4) (DNA and RNA:DNA 3'-5' helicase Lhr) (Long helicase-related protein)
