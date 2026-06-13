---
entity_id: "protein.P37194"
entity_type: "protein"
name: "slp"
source_database: "UniProt"
source_id: "P37194"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "slp b3506 JW3474"
---

# slp

`protein.P37194`

## Static

- Type: `protein`
- Source: `UniProt:P37194`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: The induction of Slp may help to stabilize the outer membrane during carbon starvation and stationary phase. Slp (starvation lipoprotein) is the product of the slp gene which forms an operon with the downstream gene dctR . Slp is believed to take part in acid resistance as expression increased when cells were grown at pH 5.5 and 4.5 under conditions known to induce glutamate-dependent acid resistance compared to pH 7.4 under the same conditions . During growth in acidic conditions, expression of Slp is negatively regulated by GadW, but positively regulated by GadXW, which are regulators of the two glutamate decarboxylase genes and the GABA APC transporter responsible for glutamate-dependent acid resistance . slp is highly induced by overexpression of EvgA , indirectly through its induction of YdeO expression , though slp was found to have a putative EvgA binding motif 542 base pairs upstream of its start codon . Under certain conditions, deletion of slp-dctR resulted in reduction of YdeO-induced acid resistance , though under conditions used to induce acid resistance naturally, slp-dctR was not necessary . A slp-dctR double mutant exhibited loss of viability during growth in spent LB at pH 2.5 much faster than wild-type . The slp-dctR double mutant was also unable to survive at pH 2.5 in minimal medium when formate, succinate, or lactate were added...

## Annotation

FUNCTION: The induction of Slp may help to stabilize the outer membrane during carbon starvation and stationary phase.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3506|gene.b3506]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37194`
- `KEGG:ecj:JW3474;eco:b3506;ecoc:C3026_18995;`
- `GeneID:948022;`
- `GO:GO:0009279; GO:0019867; GO:0042802`

## Notes

Outer membrane protein Slp
