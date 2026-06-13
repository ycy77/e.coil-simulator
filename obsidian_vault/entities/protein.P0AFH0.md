---
entity_id: "protein.P0AFH0"
entity_type: "protein"
name: "ogt"
source_database: "UniProt"
source_id: "P0AFH0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00772}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ogt b1335 JW1329"
---

# ogt

`protein.P0AFH0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFH0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00772}.

## Enriched Summary

FUNCTION: Involved in the cellular defense against the biological effects of O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme. This is a suicide reaction: the enzyme is irreversibly inactivated. Ogt is the second (after PD00230 "Ada") methyltransferase enzyme for the direct repair of alkylated DNA in Escherichia coli. The enzyme (characterized initially in E. coli B) repairs alkylated DNA (O6-methylguanine, O4-methylthymine, and O6-ethylguanine lesions) by irreversibly transferring the alkyl group to its own cysteine residue (Cys-139); it does not repair methylphosphotriesters, is not inducible and and does not trigger the adaptive response to alkylating agents . Ogt repairs O4-methylthymine lesions more effectively than O6-methylguanine in vitro . Cell extracts from a strain lacking both Ada and Ogt (Δada ogt-1::Kan) show no methyltransferase activity; Ogt is the only constitutively expressed O6-methylguanine DNA methyltransferase in E. coli; Ogt provides resistance to DNA mutation caused by low doses of alkylating agents and may protect cells prior to the induction of Ada; Ogt also protects cells from spontaneous mutations which may arise from endogenous alkylating agents present in non-dividing cells...

## Biological Role

Catalyzes 2.1.1.63-RXN (reaction.ecocyc.2.1.1.63-RXN), RXN-17824 (reaction.ecocyc.RXN-17824).

## Annotation

FUNCTION: Involved in the cellular defense against the biological effects of O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme. This is a suicide reaction: the enzyme is irreversibly inactivated.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.63-RXN|reaction.ecocyc.2.1.1.63-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17824|reaction.ecocyc.RXN-17824]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1335|gene.b1335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFH0`
- `KEGG:ecj:JW1329;eco:b1335;ecoc:C3026_07815;`
- `GeneID:945853;`
- `GO:GO:0003908; GO:0005737; GO:0006307; GO:0032259`
- `EC:2.1.1.63`

## Notes

Methylated-DNA--protein-cysteine methyltransferase (EC 2.1.1.63) (6-O-methylguanine-DNA methyltransferase) (MGMT) (O-6-methylguanine-DNA-alkyltransferase)
