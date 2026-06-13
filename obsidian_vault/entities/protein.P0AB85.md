---
entity_id: "protein.P0AB85"
entity_type: "protein"
name: "apbE"
source_database: "UniProt"
source_id: "P0AB85"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P41780, ECO:0000255|PROSITE-ProRule:PRU00303}; Lipid-anchor {ECO:0000250|UniProtKB:P41780, ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000250|UniProtKB:P41780}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "apbE yojK yojL b2214 JW5368"
---

# apbE

`protein.P0AB85`

## Static

- Type: `protein`
- Source: `UniProt:P0AB85`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P41780, ECO:0000255|PROSITE-ProRule:PRU00303}; Lipid-anchor {ECO:0000250|UniProtKB:P41780, ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000250|UniProtKB:P41780}.

## Enriched Summary

FUNCTION: Flavin transferase that catalyzes the transfer of the FMN moiety of FAD and its covalent binding to the hydroxyl group of a threonine residue in a target flavoprotein such as NqrB and NqrC, two subunits of the NQR complex. {ECO:0000250|UniProtKB:A5F5Y3}. ftp encodes a periplasmic flavin transferase which catalyses the transfer of flavin mononucleotide from FAD to target protein(s). Recombinant, purified Ftp appears to be a flavin-containing protein and is a dimer in solution . Purified Ftp flavinylates G6875-MONOMER "RsxG" in an Mg2+ dependent reaction . Ftp contains a bimetal (possibly Ca2+/Mg2+) centre . Ftp is a predicted lipoprotein . Ftp (formerly ApbE) is a component of the SoxR-reducing system; RsxABCDGE, RseC and ApbE likely form a complex that uses NAD(P)H to reduce the [2Fe-2S] center of PD04132 SoxR; a ΔabpE mutant exhibits increased expression of a EG10958 soxS promoter-linked LacZ reporter . ApbE is a periplasmic lipoprotein anchored to the inner membrane in Salmonella typhimurium; it was initially implicated in thiamine biosynthesis and iron-sulfur cluster metabolism and later shown to be a flavin transferase in Vibrio harveyii . Deleting ftp affects stop codon readthrough . apbE: alternative pyrimidine biosynthesis enzymes ftp: flavin trafficking protein . Related review:

## Biological Role

Catalyzes RXN-14461 (reaction.ecocyc.RXN-14461). Component of SoxR [2Fe-2S] reducing system (complex.ecocyc.CPLX0-10853).

## Annotation

FUNCTION: Flavin transferase that catalyzes the transfer of the FMN moiety of FAD and its covalent binding to the hydroxyl group of a threonine residue in a target flavoprotein such as NqrB and NqrC, two subunits of the NQR complex. {ECO:0000250|UniProtKB:A5F5Y3}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-14461|reaction.ecocyc.RXN-14461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-10853|complex.ecocyc.CPLX0-10853]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2214|gene.b2214]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB85`
- `KEGG:ecj:JW5368;eco:b2214;ecoc:C3026_12370;`
- `GeneID:946711;`
- `GO:GO:0005886; GO:0016740; GO:0046872; GO:1990204`
- `EC:2.7.1.180`

## Notes

FAD:protein FMN transferase (EC 2.7.1.180) (Flavin transferase)
