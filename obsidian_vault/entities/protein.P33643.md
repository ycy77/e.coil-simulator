---
entity_id: "protein.P33643"
entity_type: "protein"
name: "rluD"
source_database: "UniProt"
source_id: "P33643"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:33639093}. Note=Associates with late stage pre-50S ribosomal subunits (PubMed:33639093). {ECO:0000269|PubMed:33639093}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluD sfhB yfiI b2594 JW2576"
---

# rluD

`protein.P33643`

## Static

- Type: `protein`
- Source: `UniProt:P33643`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:33639093}. Note=Associates with late stage pre-50S ribosomal subunits (PubMed:33639093). {ECO:0000269|PubMed:33639093}.

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 1911, 1915 and 1917 in 23S ribosomal RNA (PubMed:9814761, PubMed:11087118, PubMed:11453071, PubMed:17937767). Other positions are not modified (PubMed:17937767). Uridine isomerization occurs as a late step during the assembly of the large ribosomal subunit (PubMed:17937767). Member of a network of 50S ribosomal subunit biogenesis factors (ObgE, RluD, RsfS and DarP(YjgA)) which assembles along the 30S-50S interface, allowing 23S rRNA modification and preventing incorrect 23S rRNA structures from forming (PubMed:33639093). {ECO:0000269|PubMed:11087118, ECO:0000269|PubMed:11453071, ECO:0000269|PubMed:17937767, ECO:0000269|PubMed:33639093, ECO:0000269|PubMed:9814761}. RluD is a pseudouridine synthase that catalyzes pseudouridine formation at positions 1911, 1915, and 1917 in helix 69 (H69) of the 23S rRNA . 23S rRNA modification by RluD occurs in the late assembly phase of the 50S subunit and 70S ribosome . RluD activity is involved in the resuscitation of persister cells . It may also play a role in releasing the EG11178-MONOMER from the ribosomal 30S subunit and thus contributing to fidelity of the Initiator tRNAMet selection in the P-site of the CPLX0-3964 . RluD is most active with assembled 50S ribosomal subunits; pseudouridylation of free 23S rRNA is inefficient...

## Biological Role

Catalyzes RXN-11837 (reaction.ecocyc.RXN-11837).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 1911, 1915 and 1917 in 23S ribosomal RNA (PubMed:9814761, PubMed:11087118, PubMed:11453071, PubMed:17937767). Other positions are not modified (PubMed:17937767). Uridine isomerization occurs as a late step during the assembly of the large ribosomal subunit (PubMed:17937767). Member of a network of 50S ribosomal subunit biogenesis factors (ObgE, RluD, RsfS and DarP(YjgA)) which assembles along the 30S-50S interface, allowing 23S rRNA modification and preventing incorrect 23S rRNA structures from forming (PubMed:33639093). {ECO:0000269|PubMed:11087118, ECO:0000269|PubMed:11453071, ECO:0000269|PubMed:17937767, ECO:0000269|PubMed:33639093, ECO:0000269|PubMed:9814761}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11837|reaction.ecocyc.RXN-11837]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2594|gene.b2594]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33643`
- `KEGG:ecj:JW2576;eco:b2594;ecoc:C3026_14375;`
- `GeneID:947087;`
- `GO:GO:0000027; GO:0000455; GO:0005829; GO:0009982; GO:0019843; GO:0120159; GO:0160140`
- `EC:5.4.99.23`

## Notes

Ribosomal large subunit pseudouridine synthase D (EC 5.4.99.23) (23S rRNA pseudouridine(1911/1915/1917) synthase) (Large ribosomal subunit assembly factor RluD) (rRNA pseudouridylate synthase D) (rRNA-uridine isomerase D)
