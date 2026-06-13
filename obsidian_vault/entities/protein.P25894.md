---
entity_id: "protein.P25894"
entity_type: "protein"
name: "loiP"
source_database: "UniProt"
source_id: "P25894"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}. Note=Proper membrane localization can depend on BepA."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "loiP yggG b2936 JW2903"
---

# loiP

`protein.P25894`

## Static

- Type: `protein`
- Source: `UniProt:P25894`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}. Note=Proper membrane localization can depend on BepA.

## Enriched Summary

FUNCTION: Metalloprotease that cleaves substrates preferentially between Phe-Phe residues. Plays a role in response to some stress conditions. Seems to regulate the expression of speB. {ECO:0000269|PubMed:1310091, ECO:0000269|PubMed:17651431, ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}. LoiP is an outer membrane metalloprotease that preferentially cleaves between Phe/Phe residues . LoiP is predicted to be a lipoprotein with a type II signal peptide . The protein is associated with the membrane fraction . LoiP is an outer membrane lipoprotein . LoiP has one intramolecular S-S bond plus one additional cysteine that mediates lipid attachment . Expression of loiP is upregulated in response to stress (heat shock, UV irradiation) and in an era-1 mutant background . loiP is upregulated and increased amounts of LoiP are produced when cells are grown in low osmolarity media . Overexpression of full-length loiP inhibits growth . There is no significant difference in growth between wild-type and a loiP deletion strain when grown in low osmolarity media . LoiP and G7311-MONOMER "BepA" interact and LoiP is not detected in the outer membrane fraction of a bepA null mutant (tested at 42oC in rich media containing 0.5M NaCl) . LoiP interacts directly with EG10270-MONOMER "Era", an essential GTPase . LoiP appears to enhance expression of AGMATIN-CPLX...

## Biological Role

Catalyzes RXN0-3221 (reaction.ecocyc.RXN0-3221).

## Annotation

FUNCTION: Metalloprotease that cleaves substrates preferentially between Phe-Phe residues. Plays a role in response to some stress conditions. Seems to regulate the expression of speB. {ECO:0000269|PubMed:1310091, ECO:0000269|PubMed:17651431, ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3221|reaction.ecocyc.RXN0-3221]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2936|gene.b2936]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25894`
- `KEGG:ecj:JW2903;eco:b2936;ecoc:C3026_16075;`
- `GeneID:945173;`
- `GO:GO:0004222; GO:0008237; GO:0009279; GO:0016020; GO:0034605; GO:0034644; GO:0046872; GO:0051603; GO:0071476`
- `EC:3.4.24.-`

## Notes

Metalloprotease LoiP (EC 3.4.24.-)
