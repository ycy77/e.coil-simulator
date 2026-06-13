---
entity_id: "protein.P0ABU2"
entity_type: "protein"
name: "ychF"
source_database: "UniProt"
source_id: "P0ABU2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ychF engD gtp1 b1203 JW1194"
---

# ychF

`protein.P0ABU2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABU2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: ATPase that binds to both the 70S ribosome and the 50S ribosomal subunit in a nucleotide-independent manner. Does not hydrolyze GTP. {ECO:0000255|HAMAP-Rule:MF_00944, ECO:0000269|PubMed:21527254}. The highly conserved YchF protein is a HAS-ATPase, the founding member of a family of GTP-binding proteins with ATPase activity . The conservation and essentiality of this protein in many bacteria points to an ancient origin associated with cell survival in a variety of environments . The bacterial GTPase superfamily is associated with RNA- and translation-related roles in the cell . The ATPase activity of YchF appears to be redox-regulated . YchF regulates adaptation of the cell to various stress conditions by interacting with EG10506-MONOMER, inhibiting leaderless mRNA translation and its association with the CPLX0-3953 . Additionally it inhibits production of the major stress response RPOS-MONOMER as well as polyphosphate levels via regulation of PPK-MONOMER . YchF has K+-activated ATPase activity and binds to both the 70S ribosome and the 50S ribosomal subunit in a nucleotide-independent manner . Nucleotide binding to YchF induces different conformational states. The KD of the YchF·ADPNP complex for 70S ribosomes is 3 µM, and the 70S ribosome stimulates the ATPase activity of YchF...

## Biological Role

Catalyzes ATPASE-RXN (reaction.ecocyc.ATPASE-RXN). Component of redox-responsive ATPase YchF (complex.ecocyc.CPLX0-8240).

## Annotation

FUNCTION: ATPase that binds to both the 70S ribosome and the 50S ribosomal subunit in a nucleotide-independent manner. Does not hydrolyze GTP. {ECO:0000255|HAMAP-Rule:MF_00944, ECO:0000269|PubMed:21527254}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ATPASE-RXN|reaction.ecocyc.ATPASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8240|complex.ecocyc.CPLX0-8240]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1203|gene.b1203]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABU2`
- `KEGG:ecj:JW1194;eco:b1203;ecoc:C3026_07075;`
- `GeneID:75171314;945769;`
- `GO:GO:0004857; GO:0005524; GO:0005525; GO:0005737; GO:0006979; GO:0016887; GO:0042803; GO:0043022; GO:0043023; GO:0046872`

## Notes

Ribosome-binding ATPase YchF
