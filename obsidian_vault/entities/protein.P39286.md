---
entity_id: "protein.P39286"
entity_type: "protein"
name: "rsgA"
source_database: "UniProt"
source_id: "P39286"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01820, ECO:0000269|PubMed:14973029}. Note=Associates with 30S ribosomes (PubMed:14973029). {ECO:0000269|PubMed:14973029}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsgA engC yjeQ b4161 JW4122"
---

# rsgA

`protein.P39286`

## Static

- Type: `protein`
- Source: `UniProt:P39286`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01820, ECO:0000269|PubMed:14973029}. Note=Associates with 30S ribosomes (PubMed:14973029). {ECO:0000269|PubMed:14973029}.

## Enriched Summary

FUNCTION: One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late maturation steps of the functional core of the 30S ribosomal subunit (PubMed:18223068, PubMed:21102555, PubMed:21303937, PubMed:25904134, PubMed:27382067). Binds the 30S subunit contacting the head, platform, and rRNA helix 44, which may assist the last maturation stages (PubMed:21788480, PubMed:21960487). Removes RbfA from mature, but not immature 30S ribosomes in a GTP-dependent manner; 95% removal in the presence of GTP, 90% removal in GMP-PNP and 65% removal in the presence of GDP (PubMed:21102555, PubMed:25904134). Circulary permuted GTPase that catalyzes rapid hydrolysis of GTP with a slow catalytic turnover (PubMed:12220175). Dispensible for viability, but important for overall fitness. The intrinsic GTPase activity is stimulated by the presence of 30S (160-fold increase in kcat) or 70S (96-fold increase in kcat) ribosomes (PubMed:14973029). Mature 30S ribosomes stimulate intrinsic GTPase more than do immature 30S ribosomes (PubMed:25904134). Ribosome-associated GTPase activity is stimulated by RbfA (PubMed:21102555). The GTPase is inhibited by aminoglycoside antibiotics such as neomycin and paromycin (PubMed:15466596) streptomycin and spectinomycin (PubMed:15828870). This inhibition is not due to competition for binding sites on the 30S or 70S ribosome (PubMed:15828870)...

## Biological Role

Catalyzes thiamin monophosphate phosphohydrolase (reaction.R02135), RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late maturation steps of the functional core of the 30S ribosomal subunit (PubMed:18223068, PubMed:21102555, PubMed:21303937, PubMed:25904134, PubMed:27382067). Binds the 30S subunit contacting the head, platform, and rRNA helix 44, which may assist the last maturation stages (PubMed:21788480, PubMed:21960487). Removes RbfA from mature, but not immature 30S ribosomes in a GTP-dependent manner; 95% removal in the presence of GTP, 90% removal in GMP-PNP and 65% removal in the presence of GDP (PubMed:21102555, PubMed:25904134). Circulary permuted GTPase that catalyzes rapid hydrolysis of GTP with a slow catalytic turnover (PubMed:12220175). Dispensible for viability, but important for overall fitness. The intrinsic GTPase activity is stimulated by the presence of 30S (160-fold increase in kcat) or 70S (96-fold increase in kcat) ribosomes (PubMed:14973029). Mature 30S ribosomes stimulate intrinsic GTPase more than do immature 30S ribosomes (PubMed:25904134). Ribosome-associated GTPase activity is stimulated by RbfA (PubMed:21102555). The GTPase is inhibited by aminoglycoside antibiotics such as neomycin and paromycin (PubMed:15466596) streptomycin and spectinomycin (PubMed:15828870). This inhibition is not due to competition for binding sites on the 30S or 70S ribosome (PubMed:15828870). {ECO:0000269|PubMed:12220175, ECO:0000269|PubMed:14973029, ECO:0000269|PubMed:15466596, ECO:0000269|PubMed:15828870, ECO:0000269|PubMed:21102555, ECO:0000269|PubMed:25904134, ECO:0000305|PubMed:18223068, ECO:0000305|PubMed:27382067}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - via EC:3.1.3.100
- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4161|gene.b4161]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39286`
- `KEGG:ecj:JW4122;eco:b4161;ecoc:C3026_22490;`
- `GeneID:948674;`
- `GO:GO:0000028; GO:0003924; GO:0005525; GO:0005829; GO:0019003; GO:0019843; GO:0042274; GO:0046872; GO:0097216`
- `EC:3.6.1.-`

## Notes

Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-)
