---
entity_id: "protein.P0A8M3"
entity_type: "protein"
name: "thrS"
source_database: "UniProt"
source_id: "P0A8M3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00184}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thrS b1719 JW1709"
---

# thrS

`protein.P0A8M3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8M3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00184}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: L-threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr) (PubMed:10881191, PubMed:15079065, PubMed:18997014). The rate-limiting step is amino acid activation in the presence of tRNA (PubMed:18997014). The 2'-OH of the acceptor base (adenine 76, A76) of tRNA(Thr) and His-309 collaborate to transfer L-Thr to the tRNA; substitution of 2'-OH of A76 with hydrogen or fluorine decreases transfer efficiency 760 and 100-fold respectively (PubMed:18997014). The zinc ion in the active site discriminates against charging of the isosteric amino acid valine (PubMed:10881191). Also activates L-serine, but does not detectably transfer it to tRNA(Thr) (PubMed:15079065). Edits incorrectly charged L-seryl-tRNA(Thr) via its editing domain (PubMed:15079065, PubMed:11136973, PubMed:15525511), in a post-transfer reaction probably via water-mediated hydrolysis (PubMed:15525511). {ECO:0000269|PubMed:10319817, ECO:0000269|PubMed:10881191, ECO:0000269|PubMed:11136973, ECO:0000269|PubMed:15079065, ECO:0000269|PubMed:15525511, ECO:0000269|PubMed:18997014}.; FUNCTION: ThrS is also a translational repressor protein, it controls binds its own mRNA in the operator region upstream of the start codon (PubMed:3086882)...

## Biological Role

Catalyzes L-threonine:tRNA(Thr) ligase (AMP-forming) (reaction.R03663). Component of threonine—tRNA ligase (complex.ecocyc.THRS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: L-threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr) (PubMed:10881191, PubMed:15079065, PubMed:18997014). The rate-limiting step is amino acid activation in the presence of tRNA (PubMed:18997014). The 2'-OH of the acceptor base (adenine 76, A76) of tRNA(Thr) and His-309 collaborate to transfer L-Thr to the tRNA; substitution of 2'-OH of A76 with hydrogen or fluorine decreases transfer efficiency 760 and 100-fold respectively (PubMed:18997014). The zinc ion in the active site discriminates against charging of the isosteric amino acid valine (PubMed:10881191). Also activates L-serine, but does not detectably transfer it to tRNA(Thr) (PubMed:15079065). Edits incorrectly charged L-seryl-tRNA(Thr) via its editing domain (PubMed:15079065, PubMed:11136973, PubMed:15525511), in a post-transfer reaction probably via water-mediated hydrolysis (PubMed:15525511). {ECO:0000269|PubMed:10319817, ECO:0000269|PubMed:10881191, ECO:0000269|PubMed:11136973, ECO:0000269|PubMed:15079065, ECO:0000269|PubMed:15525511, ECO:0000269|PubMed:18997014}.; FUNCTION: ThrS is also a translational repressor protein, it controls binds its own mRNA in the operator region upstream of the start codon (PubMed:3086882). The mRNA region upstream of the start codon has a tRNA-like secondary structure; mRNA and tRNA compete for binding to ThrRS (PubMed:2254931). ThrRS represses translation by preventing the ribosome from to mRNA, and tRNA(Thr) acts as an antirepressor allowing fine level control of enzyme synthesis (PubMed:2254931). X-ray structures prove that operator mRNA and tRNA bind to overlapping sites in the protein (PubMed:10319817, PubMed:11953757). {ECO:0000269|PubMed:10319817, ECO:0000269|PubMed:11953757, ECO:0000269|PubMed:2254931, ECO:0000269|PubMed:3086882}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R03663|reaction.R03663]] `KEGG` `database` - via EC:6.1.1.3
- `is_component_of` --> [[complex.ecocyc.THRS-CPLX|complex.ecocyc.THRS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1719|gene.b1719]] `RegulonDB` `S` - regulator=threonine&mdash;tRNA ligase; target=thrS; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1719|gene.b1719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8M3`
- `KEGG:ecj:JW1709;eco:b1719;ecoc:C3026_09835;`
- `GeneID:93775932;946222;`
- `GO:GO:0000049; GO:0000900; GO:0002161; GO:0003723; GO:0004812; GO:0004829; GO:0005524; GO:0005737; GO:0005829; GO:0006417; GO:0006418; GO:0006435; GO:0008270; GO:0042803; GO:0043039; GO:0045947; GO:0046677; GO:0048027`
- `EC:6.1.1.3`

## Notes

Threonine--tRNA ligase (EC 6.1.1.3) (Threonyl-tRNA synthetase) (ThrRS)
