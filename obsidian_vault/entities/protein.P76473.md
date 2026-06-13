---
entity_id: "protein.P76473"
entity_type: "protein"
name: "arnT"
source_database: "UniProt"
source_id: "P76473"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnT pmrK yfbI b2257 JW2251"
---

# arnT

`protein.P76473`

## Static

- Type: `protein`
- Source: `UniProt:P76473`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of the L-Ara4N moiety of the glycolipid undecaprenyl phosphate-alpha-L-Ara4N to lipid A. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11535604}. ArnT is a transferase that catalyzes the addition of 4-AMINO-4-DEOXY-L-ARABINOSE (L-Ara4N) residues from CPD0-1189 to lipid A. This modification confers on the organism resistance to Polymyxins "polymyxin antibiotics" (similar to the effect of lipid A modification by PHOSPHORYL-ETHANOLAMINE, which is catalyzed by EG11613-MONOMER). It should be noted that K-12 derived strains express ArnT, but do not synthesize CPD0-1189 under normal conditions, and thus are sensitive to polymyxin. The enzyme from E. coli has not been studied much, but the Salmonella typhimurium enzyme has been purified and characterized . It has been suggested, although not proven, that the enzyme is involved not only in the attachment of L-Ara4N to lipid A but also in the transport of L-Ara4N from the cytoplasm, where it is synthesized, to the periplasmic side of the inner membrane, where the attachment takes place. However, deletion of arnT results in defective attachment of L-Ara4N to the lipid A core, but does not affect the transport of undecaprenyl phosphate-α-L-Ara4N across the inner membrane...

## Biological Role

Catalyzes 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase (reaction.R09773), 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid IVA 4-amino-4-deoxy-beta-L-arabinopyranosyltransferase (reaction.R09774), 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid A 4-amino-4-deoxy-alpha-L-arabinopyranosyltransferase (reaction.R09781), RXN0-2001 (reaction.ecocyc.RXN0-2001).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the L-Ara4N moiety of the glycolipid undecaprenyl phosphate-alpha-L-Ara4N to lipid A. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11535604}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R09773|reaction.R09773]] `KEGG` `database` - via EC:2.4.2.43
- `catalyzes` --> [[reaction.R09774|reaction.R09774]] `KEGG` `database` - via EC:2.4.2.43
- `catalyzes` --> [[reaction.R09781|reaction.R09781]] `KEGG` `database` - via EC:2.4.2.43
- `catalyzes` --> [[reaction.ecocyc.RXN0-2001|reaction.ecocyc.RXN0-2001]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2257|gene.b2257]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76473`
- `KEGG:ecj:JW2251;eco:b2257;ecoc:C3026_12605;`
- `GeneID:947297;`
- `GO:GO:0000030; GO:0005886; GO:0006493; GO:0009103; GO:0009245; GO:0010041; GO:0016763; GO:0103015`
- `EC:2.4.2.43`

## Notes

Undecaprenyl phosphate-alpha-4-amino-4-deoxy-L-arabinose arabinosyl transferase (EC 2.4.2.43) (4-amino-4-deoxy-L-arabinose lipid A transferase) (Lipid IV(A) 4-amino-4-deoxy-L-arabinosyltransferase) (Polymyxin resistance protein PmrK) (Undecaprenyl phosphate-alpha-L-Ara4N transferase)
