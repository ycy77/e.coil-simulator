---
entity_id: "protein.P76257"
entity_type: "protein"
name: "yoaA"
source_database: "UniProt"
source_id: "P76257"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yoaA b1808 JW1797"
---

# yoaA

`protein.P76257`

## Static

- Type: `protein`
- Source: `UniProt:P76257`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:36509145). Has single-stranded (ss)DNA-dependent ATPase activity and 5'-3' helicase activity on forked DNA; both activities were measure in a YoaA:HolC (chi) complex (PubMed:36509145). Requires a 20-35 nucleotide (nt) 5'-ssDNA tail; dsDNA with a 20 nt gap is also unwound (PubMed:36509145). Unwinds damaged 3' nascent ends (such as those terminated by 3' azidothymidine (AZT), 3' dideoxy-C or an abasic site on the translocating strand), to promote repair and AZT excision (PubMed:36509145). Without HolC the protein has much lower activity which could be due to YoaA instability or helicase stimulation by HolC (PubMed:36509145). Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). May act in proofreading during nucleotide misincorporation, it appears to aid in the removal of potential A-to-T transversion mutations in ndk mutants (Probable) (PubMed:34181484). {ECO:0000250|UniProtKB:P27296, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}...

## Biological Role

Catalyzes RXN0-4261 (reaction.ecocyc.RXN0-4261). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:36509145). Has single-stranded (ss)DNA-dependent ATPase activity and 5'-3' helicase activity on forked DNA; both activities were measure in a YoaA:HolC (chi) complex (PubMed:36509145). Requires a 20-35 nucleotide (nt) 5'-ssDNA tail; dsDNA with a 20 nt gap is also unwound (PubMed:36509145). Unwinds damaged 3' nascent ends (such as those terminated by 3' azidothymidine (AZT), 3' dideoxy-C or an abasic site on the translocating strand), to promote repair and AZT excision (PubMed:36509145). Without HolC the protein has much lower activity which could be due to YoaA instability or helicase stimulation by HolC (PubMed:36509145). Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). May act in proofreading during nucleotide misincorporation, it appears to aid in the removal of potential A-to-T transversion mutations in ndk mutants (Probable) (PubMed:34181484). {ECO:0000250|UniProtKB:P27296, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4261|reaction.ecocyc.RXN0-4261]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1808|gene.b1808]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76257`
- `KEGG:ecj:JW1797;eco:b1808;ecoc:C3026_10300;`
- `GeneID:946305;`
- `GO:GO:0003677; GO:0003678; GO:0004386; GO:0005524; GO:0006281; GO:0009432; GO:0016887; GO:0043139; GO:0046872; GO:0051536`
- `EC:5.6.2.3`

## Notes

ATP-dependent DNA helicase YoaA (EC 5.6.2.3) (DNA 5'-3' helicase YoaA)
