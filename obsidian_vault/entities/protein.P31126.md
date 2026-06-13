---
entity_id: "protein.P31126"
entity_type: "protein"
name: "ydeE"
source_database: "UniProt"
source_id: "P31126"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydeE ydeF b1534 JW1527"
---

# ydeE

`protein.P31126`

## Static

- Type: `protein`
- Source: `UniProt:P31126`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:20067529}. YdeE is a member of the Drug:H+ Antiporter-1 (DHA) family within the Major Facilitator Superfamily (MFS) of transporters . YdeE has been implicated in arabinose efflux . YdeE is able to transport dipeptides (Ala-Gln and L-alanyl-L-branched chain amino acids) in a dipeptide overproducing strain . Overexpression of cloned ydeE (ydeF) in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of antibiotics, dyes and toxic compounds . ydeE (ydeF) is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Annotation

FUNCTION: A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:20067529}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1534|gene.b1534]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31126`
- `KEGG:ecj:JW1527;eco:b1534;ecoc:C3026_08860;`
- `GeneID:946083;`
- `GO:GO:0005886; GO:0015031; GO:0035442; GO:0071916`

## Notes

Uncharacterized MFS-type transporter YdeE
